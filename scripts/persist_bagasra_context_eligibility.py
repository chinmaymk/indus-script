"""Save seven manual context observations from the frozen Bagasra source gate."""
import json
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/bagasra_context_eligibility_v1/decision.json'


def pin(path):
    p = ROOT / path
    return dict(path=path, bytes=p.stat().st_size,
                sha256=hashlib.sha256(p.read_bytes()).hexdigest())


def main():
    if OUT.exists():
        raise FileExistsError('Refusing overwrite of frozen context decision')
    rows = [
        ('BSR2037', 'El15', '3', '100', '1998',
         'Near faience/lithic area; original use and relationship to BSR8288 unclear'),
        ('BSR5555', 'Eg2', '10', '300', '2003',
         'Map near shell workshop; narrative reports two shell-associated seals without explicit identifier allocation'),
        ('BSR6719', 'El15', None, '66', '2004',
         'Appendix trench conflicts with map Eo11; map outside wall; original-use attribution unresolved'),
        ('BSR6952', 'Ea12', '5', '70–75', '2004',
         'Map W baulk near shell area; narrative identifier allocation not explicit'),
        ('BSR7197', 'Eh1', '1', '26', '2004',
         'Gateway; authors explicitly identify likely secondary deposit'),
        ('BSR7368', 'Eh1', 'Pit1', '223', '2004',
         'Gateway pit sealed by layer1; sealed pit does not establish craft-use deposit'),
        ('BSR8288', 'El14', '4', '105', '2004',
         'Near faience/lithic area; original use and relationship to BSR2037 unclear')]
    records = [dict(field_id=i, appendix_trench=t, appendix_layer=l,
                    depth_cm_below_datum=d, figure4_year=y,
                    observation=o, primary_pages=[7,15,18],
                    independently_classified_original_use=None,
                    eligible_matched_deposit=False) for i,t,l,d,y,o in rows]
    sources = ['data/processed/bagasra_context_eligibility_protocol_v1.json',
        'data/raw/bagasra-jamison2017-publisher.pdf',
        'data/raw/bagasra-bhan2005-web-capture.json',
        'data/raw/bagasra-sonawane2003-search-capture.json',
        'results/bagasra_context_eligibility_v1/paper_extracted_text.txt',
        'scripts/persist_bagasra_context_eligibility.py']
    sources += [f'results/bagasra_context_eligibility_v1/page{p}.png' for p in (7,15,18)]
    result = dict(date='2026-10-11', status='closed_test_unavailable',
        selection='Complete published seven-seal frame; no replacements',
        records=records,
        source_conflicts=[dict(field_id='BSR6719', figure4_trench='Eo11',
            appendix1_trench='El15', depth_agrees_cm='66',
            resolution='Unresolved; preserve both primary claims, no guessed correction')],
        craft_evidence=dict(shell='Bhan2005 reports workshop with shell wasters, unfinished bangles and raw shells',
            faience='Bhan2005 reports quartz powder, burning and manufacturing evidence',
            bead_lithic='Bhan2005 distinguishes bead manufacture from stockpiles; absence of some jasper waste prevents equating all stockpiles with on-site manufacture',
            limitation='Craft presence does not establish original use or meanings of nearby seals'),
        eligible_replicated_contrast=False, sign_scoring_executed=False,
        outcome='No secured replicated original-use bead versus shell/faience deposit contrast; proposed transfer test unavailable',
        missing='Object-specific depositional records resolving secondary movement, phase/event links, comparable recovery and contrasting deposits',
        acquisition=dict(publisher='Web tool timed out; one direct HTTP acquisition succeeded with 21-page PDF',
            supporting_report='Bhan2005 primary Antiquity web extraction retained',
            second_cited_report='Exact Sonawane2003 search found request-only record; no original acquired or request sent',
            discovery='Four internal-review discovery queries and returned source URLs reported in research log; original tool responses not retained, no reconstructed raw capture claimed'),
        exposure='Figure4 includes seal photographs, viewed for context labels. No signs transcribed/scored; no blinding or unseen-holdout claim.',
        constraints=['No proximity threshold converted into working-floor association',
            'Unequal layers/depths are not proven comparable phases',
            'All seven are one published site assemblage, not seven independent replicated deposits',
            'Gate failure is not semantic falsification',
            'Seal masses in appendix are physical seal measurements, not encoded quantity calibration',
            'No p value, translation, corpus amendment or phonetic/semantic assignment'],
        evidence_pins=[pin(p) for p in sources])
    OUT.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(result['outcome'])


if __name__ == '__main__':
    main()
