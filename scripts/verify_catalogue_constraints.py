"""Independent finite-model/source-scope check of ten selected catalogue targets.

Uses only Python's standard library, imports no producer code, and reconstructs
selected targets from source reviews before reading the producer result. Exhaustive
subset consistency checks independently find inclusion-minimal contradictions.
This checks recorded local catalogue evidence, not primary-image truth or semantics.
"""
import csv
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'results/catalogue_constraint_independent.json'


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def run():
    errors, checks, checked_pins, visited = [], [], [], set()
    def check(name, value, detail=None):
        checks.append({'check': name, 'passed': bool(value), 'detail': detail})
        if not value:
            errors.append(name)
    def read(name):
        return json.loads((ROOT / name).read_text())
    def review(stem):
        return read('data/processed/' + stem + '_review.json')
    def pins(name):
        if name in visited:
            return
        visited.add(name)
        obj = read(name)
        for pin in obj.get('evidence_files', []):
            path = ROOT / pin['path']
            exists = path.is_file()
            hash_ok = exists and digest(path) == pin['sha256']
            size_ok = exists and ('bytes' not in pin or path.stat().st_size == pin['bytes'])
            checked_pins.append({'parent': name, 'path': pin['path'],
                                 'hash_matches': hash_ok, 'size_matches_if_recorded': size_ok})
            check('evidence pin ' + name + ' -> ' + pin['path'], hash_ok and size_ok)
            if exists and pin['path'].endswith('_review.json'):
                pins(pin['path'])

    names = ['pincer_primary', 'ending_mapping', 'comb_variation', 'double_grid_primary',
             'w525_primary', 'm735_primary', 'h133_w554_primary', 'm897_mapping']
    r = {name: review(name) for name in names}
    rows = {}
    # Select metadata/text columns only; proposed translations are not evidence.
    with (ROOT / 'data/raw/lipi_inscriptions.csv').open(newline='') as handle:
        for row in csv.DictReader(handle):
            if row['id'] in {'3329.1', '3159.1'} or row['cisi'] == 'L-89':
                rows[row['id']] = {key: row[key] for key in ('id', 'cisi', 'excavation-idno', 'text')}
    targets = []
    def add(identifier, w, ms, name, object_ref, evidence_field):
        targets.append({'id': identifier, 'W': w, 'M': list(ms),
                        'review': 'data/processed/' + name + '_review.json',
                        'primary_object_reference': object_ref, 'source_field': evidence_field})

    p = r['pincer_primary']
    check('pincer selected object identity', p['artifact']['excavation'] == 'DK8333' and p['artifact']['M77_text'] == '3068')
    for w in ('W550', 'W555'):
        selected = [x for x in p['local_target_correspondences'] if x['W'] == w]
        check('exactly one explicit pincer target ' + w, len(selected) == 1)
        if selected:
            add('M63_' + w, w, [selected[0]['M']], 'pincer_primary', 'DK8333/M77:3068', 'local_target_correspondences')
    p = r['ending_mapping']
    bridge = p['primary_artifact_bridge']
    check('L89 explicit object identity', bridge['excavation'] == '15337' and bridge['M77_text'] == '7090')
    check('L89 comb target explicitly stated', 'comb to M254' in bridge['finding'])
    check('L89 raw W527 occurs at selected comb end', any(x['cisi'] == 'L-89' and x['text'].startswith('+527-') for x in rows.values()))
    add('L89_W555', p['catalogue_conflict']['observed_ending_W'], [p['catalogue_conflict']['primary_comparison_M']],
        'ending_mapping', '15337/M77:7090', 'catalogue_conflict.observed_ending_W/primary_comparison_M')
    # Only the explicitly discussed comb target is extracted; other candidate codes remain unused.
    add('L89_W527', 'W527', [bridge['M77_candidate_reading_order'][-1]], 'ending_mapping',
        '15337/M77:7090', 'primary_artifact_bridge.finding and final candidate target; raw L89 comb code')
    p = r['comb_variation']
    m934 = review('m934_primary')
    check('MIC158 old-publication identity', p['primary_identity']['excavation'] == 'DM50' and
          p['primary_identity']['MIC_seal'] == '158' and p['primary_identity']['M77_text'] == '1158')
    check('M934 alias left unverified in frozen input reviews', p['primary_identity']['CISI_M934_label_primary_verified'] is False and
          m934['identity_status']['CISI2_M934_metadata_primary_verified'] is False)
    check('M934 raw selected target and old-publication locator', rows['3329.1']['text'] == m934['secondary_text'] and
          rows['3329.1']['text'].startswith('+526-') and rows['3329.1']['excavation-idno'] == 'DM50158')
    add('MIC158_W526', 'W526', [p['observed_normalized_reading_order'][-1]], 'comb_variation',
        'DM50/MIC158/M77:1158', 'comb-context target plus nested m934 primary review/raw row3329.1; qualified alias')
    p = r['double_grid_primary']
    check('double grid local span only', p['span_alignment_scope'] == 'This authenticated artifact only' and
          not p['global_W617_expansion_established'] and not p['ancient_grapheme_segmentation_established'])
    add('M81_W617', p['span_alignment']['W'][0], p['span_alignment']['M'], 'double_grid_primary',
        'C3133/MIC180/M77:1180', 'span_alignment')
    for case in r['w525_primary']['cases']:
        if case['status'] == 'supported_local_catalogue_correspondence':
            check('W525 alias qualification ' + case['secondary_cisi'], case['modern_CISI_entry_independently_checked'] is False)
            add(case['secondary_cisi'] + '_W525', 'W525', [case['local_W525_to']], 'w525_primary',
                case['field_number'] + '/M77:' + str(case['m77_reference']), 'cases[].local_W525_to with supported status')
    check('conflicting H1123 remains excluded', not any(x['id'].startswith('H-1123') for x in targets))
    p = r['m735_primary']
    check('MIC60 old-publication identity', (p['primary_excavation'], p['primary_item'], p['M77_reference']) == ('C3070', 60, 1060))
    check('M735 secondary raw target retained', rows['3159.1']['text'].endswith('-195+') and
          rows['3159.1']['excavation-idno'] == p['secondary_raw_excavation'])
    check('M735 alias and row dependency preserved in source', 'contingent on secondary row identity' in p['correspondence_status'] and
          'not independently checked' in p['correspondence_status'])
    add('MIC60_W195', p['local_target'], [p['local_M']], 'm735_primary', 'C3070/MIC60/M77:1060', 'local_target/local_M')
    p = r['h133_w554_primary']
    check('H133 target-only scope', p['full_numbered_transcription_independently_audited'] is False and
          p['modern_CISI_alias_independently_checked'] is False)
    add('EH261_W554', p['target_correspondence']['W'], [p['target_correspondence']['M']], 'h133_w554_primary',
        '8360/EH261/M77:4261', 'target_correspondence only')
    check('exactly ten selected targets', len(targets) == 10 and len({x['id'] for x in targets}) == 10)
    uncertain = {'id': 'FEM545_W550_uncertain', 'W': 'W550', 'M': ['M222'],
                 'review': 'data/processed/m897_mapping_review.json',
                 'primary_object_reference': 'DK9111/FEM545/M77:2545'}
    check('uncertain M897 source still unresolved', 'unresolved' in r['m897_mapping']['scope'] and
          r['m897_mapping']['normalized_reading_order'][-2] == 'M222')
    m897_original = review('m897_primary')
    check('uncertain M897 W550 remains a secondary unresolved label',
          m897_original['raw_text'].split('-')[1] == '550' and
          m897_original['verified']['fine_W550_identity'] is False and
          m897_original['primary']['field_number'] == 'DK9111')
    check('uncertain target not core', uncertain['id'] not in {x['id'] for x in targets})

    # Construct finite functions/relations from sets, independently of producer pair rules.
    def consistent(subset, model):
        maximum = 1 if model in {'bijective_single', 'deterministic_single'} else 2
        forward = {}
        inverse = {}
        for a in subset:
            span = tuple(a['M'])
            if len(span) < 1 or len(span) > maximum:
                return False
            forward.setdefault(a['W'], set()).add(span)
            inverse.setdefault(span, set()).add(a['W'])
        if model != 'span_relation' and any(len(images) > 1 for images in forward.values()):
            return False
        if model == 'bijective_single' and any(len(preimages) > 1 for preimages in inverse.values()):
            return False
        return True

    models = ['bijective_single', 'deterministic_single', 'deterministic_span', 'span_relation']
    def exhaustive(population, model):
        minimal = []
        for size in range(len(population) + 1):
            for group in itertools.combinations(population, size):
                ids = frozenset(x['id'] for x in group)
                if any(previous <= ids for previous in minimal):
                    continue
                if not consistent(group, model):
                    minimal.append(ids)
        return {'satisfiable_on_these_assertions': consistent(population, model),
                'minimal_contradiction_sets': sorted([sorted(x) for x in minimal], key=lambda x: (len(x), x)),
                'all_minimal_sets_are_singletons_or_pairs': all(len(x) <= 2 for x in minimal),
                'possible_subsets': 2 ** len(population)}

    outcomes = {label: {m: exhaustive(pop, m) for m in models} for label, pop in
                [('core_local_targets', targets), ('with_uncertain_M897', targets + [uncertain])]}
    # Read the result only after independent reconstruction and solving.
    audit_name = 'results/catalogue_constraint_audit.json'
    audit = read(audit_name)
    expected_models = {
        'bijective_single': {'max_span': 1, 'deterministic': True, 'injective': True},
        'deterministic_single': {'max_span': 1, 'deterministic': True, 'injective': False},
        'deterministic_span': {'max_span': 2, 'deterministic': True, 'injective': False},
        'span_relation': {'max_span': 2, 'deterministic': False, 'injective': False},
    }
    check('reported model definitions match independently tested meanings', audit['models'] == expected_models)
    compare_fields = ['id', 'W', 'M', 'review', 'primary_object_reference']
    simplify = lambda xs: sorted([{k: x[k] for k in compare_fields} for x in xs], key=lambda x: x['id'])
    check('all ten reconstructed assertions match producer', simplify(targets) == simplify(audit['core_assertions']))
    check('separate sensitivity assertion matches', all(audit['uncertain_sensitivity_assertion'][k] == uncertain[k] for k in compare_fields))
    check('M934 alias qualification retained in output', 'not separately checked' in next(x['scope'] for x in audit['core_assertions'] if x['id'] == 'MIC158_W526'))
    check('M735 row dependency retained in output', next(x['scope'] for x in audit['core_assertions'] if x['id'] == 'MIC60_W195') == r['m735_primary']['correspondence_status'])
    for population, result in outcomes.items():
        for model, solved in result.items():
            reported = audit['outcomes'][population][model]
            supplied = sorted([sorted(w['assertion_ids']) for w in reported['minimal_contradiction_witnesses']], key=lambda x: (len(x), x))
            check('minimal sets ' + population + '/' + model, supplied == solved['minimal_contradiction_sets'])
            check('satisfiability ' + population + '/' + model, reported['satisfiable_on_these_assertions'] == solved['satisfiable_on_these_assertions'])
    expected_coverage = []
    for number in range(1, 418):
        m = f'M{number:03d}'
        ids = [x['id'] for x in targets if m in x['M']]
        expected_coverage.append({'M': m, 'local_assertion_ids': ids,
                                  'semantic_value': None, 'phonetic_value': None,
                                  'status': 'local catalogue evidence only' if ids else 'not constrained by this selected audit'})
    check('all 417 coverage entries and null values match', expected_coverage == audit['M_inventory_coverage'])
    check('all 417 codes present exactly once', [x['M'] for x in audit['M_inventory_coverage']] == [f'M{i:03d}' for i in range(1, 418)])
    check('no uncertain assertion enters any coverage row', all(uncertain['id'] not in x['local_assertion_ids'] for x in audit['M_inventory_coverage']))
    unique = {}
    for a in targets:
        unique.setdefault((a['W'], tuple(a['M'])), []).append(a['id'])
    expected_unique = [{'W': w, 'M': list(ms), 'assertion_ids': ids} for (w, ms), ids in sorted(unique.items())]
    check('deduplication preserves all supporting assertion IDs', expected_unique == audit['deduplicated_W_to_span_assertions'])
    expected_summary = {'core_local_assertions': len(targets), 'distinct_W_to_span_assertions': len(unique),
                        'constrained_W_codes': sorted({x['W'] for x in targets}),
                        'M_members': sorted({m for x in targets for m in x['M']}), 'M_inventory_members': 417}
    check('summary equals independent reconstruction', expected_summary == audit['summary'])
    for path, expected_hash in audit['input_sha256'].items():
        check('producer input pin ' + path, (ROOT / path).is_file() and digest(ROOT / path) == expected_hash)
    for name in names:
        pins('data/processed/' + name + '_review.json')
    check('no semantic/global claims in result', audit['established_semantic_values'] == 0 and
          audit['established_phonetic_values'] == 0 and audit['global_conversion_promoted'] is False)
    output = {'schema_version': 1, 'passed': not errors, 'failed_checks': errors,
              'scope': 'Independent reconstruction of ten recorded local targets and finite-model verification; no new primary-image authentication or global catalogue conversion.',
              'independence': 'No producer import. Targets reconstructed from named reviews plus selected raw metadata columns. Set-based function/relation construction and exhaustive subsets find inclusion-minimal contradictions.',
              'reconstructed_core_assertions': targets, 'uncertain_sensitivity_assertion': uncertain,
              'outcomes': outcomes, 'M_inventory_coverage': expected_coverage,
              'summary': expected_summary, 'checks': checks, 'source_evidence_pins_checked': checked_pins,
              'alias_limits': {'M934': 'Frozen inputs link MIC158/DM50 to M77:1158 and leave the modern CISI alias unchecked. Later m934_cisi2_review.json supplies labelled photographs but retains DM56/DM50 conflict. W526 remains secondary row3329.1, not a newly certified fine-stroke label; these ten constraints are unchanged.',
                               'M735': 'Frozen input review links MIC60/C3070 to M77:1060 and leaves the modern alias unchecked. Later m735_alias_followup.json is separate evidence and does not alter these ten frozen constraints.'},
              'logical_limits': ['Bijective label means a locally injective partial one-to-one correspondence; no global surjectivity, W-inventory cardinality or completion to full inventories is tested.',
                                 'Satisfiable selected constraints do not establish validity elsewhere.',
                                 'Recorded assertions and primary evidence truth are distinct; hashes authenticate file identity, not historical correctness.',
                                 'M897 remains sensitivity-only and cannot change core conclusions.',
                                 'No candidate sequence beyond the ten selected targets was promoted.'],
              'new_downloads': [], 'established_semantic_values': 0, 'established_phonetic_values': 0,
              'input_sha256': {path: digest(ROOT / path) for path in
                               [audit_name, 'scripts/audit_catalogue_constraints.py', 'scripts/verify_catalogue_constraints.py',
                                'data/raw/lipi_inscriptions.csv', *sorted(visited)]}}
    OUTPUT.write_text(json.dumps(output, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps({'passed': output['passed'], 'failed_checks': errors,
                      'checks': len(checks), 'evidence_pin_checks': len(checked_pins),
                      'summary': expected_summary,
                      'minimal_set_counts': {pop: {m: len(v['minimal_contradiction_sets']) for m, v in rs.items()} for pop, rs in outcomes.items()}}, indent=2))
    return 0 if output['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(run())
