#!/usr/bin/env python3
"""Capture usage metadata only, then tally a frozen research cutoff without prompts."""
import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re


KEYS = ('input_tokens', 'cached_input_tokens', 'cache_write_input_tokens',
        'output_tokens', 'reasoning_output_tokens', 'total_tokens')
ROOTS = ['01a0cb0a-c3d3-7290-a6bb-752a686c8f57',
         '01a12a06-ffd2-7371-a682-3309f96488ce']


def canonical_usage(value, claude=False):
    if claude:
        cached = value.get('cache_read_input_tokens', 0)
        written = value.get('cache_creation_input_tokens', 0)
        inp = value.get('input_tokens', 0) + cached + written
        out = value.get('output_tokens', 0)
        reason = value.get('output_tokens_details', {}).get('thinking_tokens', 0)
        return dict(zip(KEYS, (inp, cached, written, out, reason, inp + out)))
    result = {k: value.get(k, 0) for k in KEYS}
    assert result['total_tokens'] == result['input_tokens'] + result['output_tokens']
    return result


def sum_usage(rows):
    return {k: sum(r['usage'][k] for r in rows) for k in KEYS}


def add_unique(store, key, row):
    if key in store:
        old = store[key]
        assert old['usage'] == row['usage'], ('conflicting duplicate', key)
        assert old['model'] == row['model'], ('conflicting model', key)
        return False
    store[key] = row
    return True


def bounded_lines(path):
    """Hash and parse a fixed byte prefix, even if a live log grows during capture."""
    size = path.stat().st_size
    digest = hashlib.sha256()
    remaining = size
    malformed = []
    line_number = 0
    with path.open('rb') as stream:
        while remaining:
            line = stream.readline(remaining)
            if not line:
                raise RuntimeError(f'Source shrank during capture: {path}')
            remaining -= len(line)
            digest.update(line)
            line_number += 1
            try:
                event = json.loads(line)
            except (ValueError, UnicodeDecodeError) as error:
                match = re.search(rb'"type"\s*:\s*"([^"]+)"', line[:256])
                apparent_type = match.group(1).decode() if match else None
                if apparent_type == 'token_usage_record':
                    raise RuntimeError(f'Malformed usage record: {path}:{line_number}') from error
                malformed.append({'line': line_number, 'bytes': len(line),
                                  'apparent_type': apparent_type,
                                  'sha256': hashlib.sha256(line).hexdigest(),
                                  'error': str(error)})
                continue
            yield event
    yield {'_source': {'path': str(path), 'snapshot_bytes': size,
                      'snapshot_sha256': digest.hexdigest(),
                      'malformed_nonusage_lines': malformed}}


def capture(args):
    cutoff = args.cutoff
    metas, paths = {}, {}
    for folder in ['sessions', 'archived_sessions']:
        for path in (args.codex_home / folder).rglob('*.jsonl'):
            with path.open() as stream:
                meta = json.loads(next(stream))['payload']
            tid = meta['id']
            if tid in paths:
                raise RuntimeError(f'Duplicate session history: {tid}')
            metas[tid], paths[tid] = meta, path
    selected = set(ROOTS)
    while True:
        added = set()
        for tid, meta in metas.items():
            source = meta.get('source')
            parent = meta.get('parent_thread_id')
            if not parent and isinstance(source, dict):
                parent = source.get('subagent', {}).get('thread_spawn', {}).get('parent_thread_id')
            if parent in selected:
                added.add(tid)
        if added <= selected:
            break
        selected |= added
    missing = selected - paths.keys()
    assert not missing, ('missing root history', sorted(missing))

    rows, sources, threads, checks = {}, [], [], []
    duplicates = 0
    for tid in sorted(selected):
        meta = metas[tid]
        model, last_cumulative, last_event = None, None, None
        owned = []
        for event in bounded_lines(paths[tid]):
            if '_source' in event:
                sources.append(event['_source'])
                continue
            payload = event.get('payload', {})
            if event.get('timestamp', '') > cutoff:
                continue
            if event.get('type') == 'turn_context':
                model = payload.get('model') or model
            if event.get('type') == 'event_msg' and payload.get('type') == 'token_count':
                info = payload.get('info')
                if info:
                    last_event = info['total_token_usage']['total_tokens']
            if event.get('type') != 'token_usage_record' or payload.get('thread_id') != tid:
                continue
            assert model, ('usage without model context', tid)
            row = {'provider': 'openai', 'model': model, 'thread_id': tid,
                   'request_id': payload['response_id'], 'timestamp': event['timestamp'],
                   'usage': canonical_usage(payload['usage'])}
            if add_unique(rows, ('openai', row['request_id']), row):
                owned.append(row)
            else:
                duplicates += 1
            last_cumulative = canonical_usage(payload['thread_token_usage'])
        total = sum_usage(owned)
        if owned:
            assert total == last_cumulative, ('per-call/cumulative mismatch', tid)
        source = meta.get('source')
        guardian = isinstance(source, dict) and source.get('subagent', {}).get('other') == 'guardian'
        threads.append({'id': tid, 'parent_thread_id': meta.get('parent_thread_id'),
                        'created_at': meta['timestamp'],
                        'role': 'automatic_review' if guardian else ('root' if tid in ROOTS else 'research_subagent'),
                        'usage_records': len(owned), 'usage': total})
        checks.append({'thread_id': tid, 'per_call_equals_record_cumulative': True if owned else None,
                       'last_legacy_event_total': last_event,
                       'record_total': total['total_tokens'],
                       'legacy_matches_records': last_event == total['total_tokens'] if owned else None})

    claude_messages, claude_sessions = {}, set()
    claude_duplicates = 0
    for path in sorted(args.claude_project.rglob('*.jsonl')):
        for event in bounded_lines(path):
            if '_source' in event:
                sources.append(event['_source'])
                continue
            if event.get('timestamp', '') > cutoff:
                continue
            message = event.get('message')
            if not isinstance(message, dict) or not message.get('usage'):
                continue
            if message.get('model') == '<synthetic>':
                continue
            assert event.get('cwd') == str(args.repo)
            row = {'provider': 'anthropic', 'model': message['model'],
                   'thread_id': event['sessionId'], 'request_id': message['id'],
                   'timestamp': event['timestamp'],
                   'usage': canonical_usage(message['usage'], claude=True)}
            if not add_unique(claude_messages, ('anthropic', row['request_id']), row):
                claude_duplicates += 1
            claude_sessions.add(event['sessionId'])
    rows.update(claude_messages)
    envelopes = []
    envelope_seen = set()
    for path in sorted((args.repo / 'data/raw').glob('*claude*.json')):
        value = json.loads(path.read_text())
        if value.get('type') != 'result' or 'usage' not in value:
            continue
        sid = value['session_id']
        assert sid not in claude_sessions, ('overlapping aggregate and message ledger', sid)
        assert sid not in envelope_seen, ('duplicate aggregate session', sid)
        envelope_seen.add(sid)
        # These pinned envelopes are Oct 10 calls, before the Oct 11 cutoff.
        assert 'oct10' in path.name
        aggregate = canonical_usage(value['usage'], claude=True)
        converted = []
        for name, usage in value.get('modelUsage', {}).items():
            u = canonical_usage({'input_tokens': usage.get('inputTokens', 0),
                                 'cache_read_input_tokens': usage.get('cacheReadInputTokens', 0),
                                 'cache_creation_input_tokens': usage.get('cacheCreationInputTokens', 0),
                                 'output_tokens': usage.get('outputTokens', 0),
                                 'output_tokens_details': {'thinking_tokens': usage.get('thinkingTokens', 0)}}, True)
            row = {'provider': 'anthropic', 'model': name, 'thread_id': sid,
                   'request_id': sid + ':' + name, 'timestamp': None,
                   'usage': u, 'source_path': str(path.relative_to(args.repo)),
                   'record_scope': 'nonoverlapping CLI session aggregate'}
            converted.append(row)
            add_unique(rows, ('anthropic_aggregate', row['request_id']), row)
        assert sum_usage(converted) == aggregate
        blob = path.read_bytes()
        sources.append({'path': str(path), 'snapshot_bytes': len(blob),
                        'snapshot_sha256': hashlib.sha256(blob).hexdigest()})
        envelopes.append({'path': str(path.relative_to(args.repo)), 'session_id': sid,
                          'is_error': value.get('is_error'), 'usage': aggregate})
    return {'schema_version': 1, 'captured_at_utc': datetime.now(timezone.utc).isoformat(),
            'cutoff_utc': cutoff, 'research_roots': ROOTS,
            'excluded_roots': {'blog_and_accounting': '01a12a08-25a3-74e2-98e5-91f85089bfa8',
                               'unrelated_grammar': '01a0d54b-7ac3-7901-a7bb-0750f9bbc56d'},
            'source_snapshots': sources, 'threads': threads, 'checks': checks,
            'deduplicated_openai_records': duplicates,
            'deduplicated_claude_message_blocks': claude_duplicates,
            'cli_envelopes': envelopes, 'records': list(rows.values()),
            'coverage': 'Retained local research histories and saved CLI envelopes only; no claim of complete provider billing.'}


def summarize(value):
    grouped = defaultdict(list)
    for row in value['records']:
        grouped[row['model']].append(row)
    models = {name: {'usage': sum_usage(rows), 'records': len(rows),
                     'sessions': len({r['thread_id'] for r in rows})}
              for name, rows in sorted(grouped.items())}
    primary = [r for r in value['records'] if r['model'] != 'codex-auto-review']
    overhead = [r for r in value['records'] if r['model'] == 'codex-auto-review']
    total = sum_usage(value['records'])
    return {'cutoff_utc': value['cutoff_utc'], 'coverage': value['coverage'],
            'models': models, 'research_models': sum_usage(primary),
            'automatic_review': sum_usage(overhead), 'all_recorded_research': total,
            'tokens_excluding_cache_reads': total['total_tokens'] - total['cached_input_tokens'],
            'thread_roles': dict(Counter(t['role'] for t in value['threads'])),
            'threads_with_no_usage_records': sum(t['usage_records'] == 0 for t in value['threads']),
            'reconciled_threads': sum(t['usage_records'] > 0 for t in value['threads']),
            'legacy_counter_mismatches': sum(c['legacy_matches_records'] is False for c in value['checks']),
            'malformed_nonusage_lines': sum(len(s.get('malformed_nonusage_lines', [])) for s in value['source_snapshots']),
            'deduplicated_claude_message_blocks': value['deduplicated_claude_message_blocks']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--capture', type=Path)
    parser.add_argument('--from-capture', type=Path)
    parser.add_argument('--report', type=Path, required=True)
    parser.add_argument('--cutoff', default='2026-10-11T08:23:38.418Z')
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--codex-home', type=Path, default=Path('/Users/chinmaymk/.codex'))
    parser.add_argument('--claude-project', type=Path,
                        default=Path('/Users/chinmaymk/.claude/projects/-Users-chinmaymk-github-indus-script'))
    args = parser.parse_args()
    assert bool(args.capture) != bool(args.from_capture)
    assert not args.report.exists(), 'Use a new report path; frozen outputs are preserved.'
    if args.capture:
        assert not args.capture.exists(), 'Capture already exists.'
        value = capture(args)
        args.capture.parent.mkdir(parents=True, exist_ok=True)
        args.capture.write_text(json.dumps(value, separators=(',', ':')) + '\n')
    else:
        value = json.loads(args.from_capture.read_text())
    report = summarize(value)
    report['capture_sha256'] = hashlib.sha256((args.capture or args.from_capture).read_bytes()).hexdigest()
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
