"""Correct the whitespace-only observation defect without rerunning author code."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / 'results/yajnadevam_validation_v1/intersection_control'


def main():
    old = json.loads((DIR / 'result.json').read_text())
    for p in old['pins']:
        b = (ROOT / p['path']).read_bytes()
        assert len(b) == p['bytes'] and hashlib.sha256(b).hexdigest() == p['sha256']
    text = (DIR / 'stdout.txt').read_text()
    values = re.findall(r'^003-d-bow:\s*=\s*(.*?)\s*$', text, re.MULTILINE)
    assert old['exit_code'] == 0 and values == ['j']
    assert [r['cumulative_candidates'] for r in old['independent_rows']] == [['d'], [], [], []]
    result = dict(
        date='2026-10-11', bug_reproduced=True,
        scope='Original program intersection soundness; not ancient readings or Sanskrit validity',
        program_invocations=1, rerun=False, original_program_and_regexes_unchanged=True,
        final_original_candidates=values, correct_cumulative_candidates=[],
        observation_defect='Initial driver required one space before =; original comment removal leaves two. Saved original stdout already contains final j.',
        initial_observation_preserved=str((DIR / 'result.json').relative_to(ROOT)),
        corrected_conclusion='Empty-set reset reproduced: final j violates earlier row; original output is not a cumulative-intersection proof',
        pins=[])
    for p in [DIR / 'result.json', DIR / 'stdout.txt', Path(__file__).resolve()]:
        b=p.read_bytes()
        result['pins'].append(dict(path=str(p.relative_to(ROOT)),bytes=len(b),sha256=hashlib.sha256(b).hexdigest()))
    out=DIR / 'observation_review.json'
    if out.exists():
        raise FileExistsError('Frozen observation review already exists')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('Empty-set reset reproduced from saved original output; no author-code rerun')


if __name__ == '__main__':
    main()
