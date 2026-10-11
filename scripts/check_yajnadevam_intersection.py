"""One frozen algorithmic counterexample; original author code and rows unchanged."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = ROOT / 'data/processed/yajnadevam_intersection_control_protocol_v1.json'
OUT = ROOT / 'results/yajnadevam_validation_v1/intersection_control'


def pin(p):
    return dict(path=str(p.relative_to(ROOT)), bytes=p.stat().st_size,
                sha256=hashlib.sha256(p.read_bytes()).hexdigest())


def main():
    protocol = json.loads(PROTOCOL.read_text())
    for expected in protocol['pins']:
        assert pin(ROOT / expected['path']) == expected
    if OUT.exists():
        raise FileExistsError('Refusing overwrite or repeated frozen run')
    source = ROOT / 'data/raw/yajnadevam-prove-oct11.pl'
    corpus = (ROOT / 'data/raw/yajnadevam-testcorpus-oct11.txt').read_text()
    block = re.search(r'^003-d-bow:.*?(?=^004-a-man:)', corpus,
                      re.MULTILINE | re.DOTALL).group()
    (OUT / 'data').mkdir(parents=True)
    (OUT / 'data/testcorpus.txt').write_text(block)
    dictionary = ['and', 'ja', 'jja']
    (OUT / 'mw.txt').write_text('\n'.join(dictionary) + '\n')
    run = subprocess.run(['/usr/bin/perl', str(source)], cwd=OUT,
                         capture_output=True, text=True, timeout=10)
    (OUT / 'stdout.txt').write_text(run.stdout)
    (OUT / 'stderr.txt').write_text(run.stderr)
    rows, intersection = [], None
    for line in block.splitlines()[1:]:
        if not line.strip():
            continue
        cisi, inscr, regex = line.split()
        found = [(word, re.fullmatch(regex, word)) for word in dictionary]
        candidates = sorted({m.group(1) for word, m in found if m})
        intersection = set(candidates) if intersection is None else intersection & set(candidates)
        rows.append(dict(cisi=cisi, source_sign_string=inscr, source_regex=regex,
                         candidates=candidates, cumulative_candidates=sorted(intersection)))
    assert [r['cumulative_candidates'] for r in rows] == protocol['prediction']['sound_intersection_after_rows']
    final = [s for s in run.stdout.splitlines() if s.startswith('003-d-bow: =')]
    reproduced = run.returncode == 0 and final == ['003-d-bow: = j']
    result = dict(scope='Algorithmic cumulative-intersection soundness only; no Sanskrit or historical truth test',
                  invocation=['/usr/bin/perl', str(source)], exit_code=run.returncode,
                  original_rows_unchanged=True, original_program_unchanged=True,
                  dictionary_kind='controlled toy fixture, not original Sanskrit dictionary',
                  independent_rows=rows, original_final_lines=final,
                  bug_reproduced=reproduced,
                  conclusion='Original program returns j despite incompatible earlier constraint' if reproduced else 'Prediction not reproduced; investigate before conclusion',
                  pins=[pin(p) for p in (PROTOCOL, source, OUT / 'data/testcorpus.txt', OUT / 'mw.txt',
                                        OUT / 'stdout.txt', OUT / 'stderr.txt', Path(__file__).resolve())])
    (OUT / 'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('exit_code','bug_reproduced','original_final_lines','conclusion')}))
    if not reproduced:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
