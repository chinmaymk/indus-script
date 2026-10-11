"""Record software, script and result hashes after successful pipeline completion."""
from importlib.metadata import version
import argparse
from datetime import date
import platform
from common import ROOT,sha256,write_json

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--research-date', default=date.today().isoformat())
    parser.add_argument('--validation-scope', default='File snapshot only; consult execution logs for validation coverage.')
    args=parser.parse_args()
    files=sorted(p for folder in ['scripts','tests','docs'] for p in (ROOT/folder).glob('*') if p.is_file() and p.name != ".DS_Store")
    # The pipeline can still be writing its redirected log while this step runs.
    outputs=sorted(p for p in (ROOT/'results').rglob('*') if p.is_file() and p.name not in ('run_manifest.json','last_run.log','latest_run.log','.DS_Store'))
    processed=sorted(p for p in (ROOT/'data/processed').rglob('*') if p.is_file() and p.name != ".DS_Store")
    write_json('results/run_manifest.json',{
        'research_started_date':'2026-09-22', 'research_date':args.research_date, 'python':platform.python_version(),
        'validation_scope':args.validation_scope,
        'numpy':version('numpy'), 'Pillow':version('Pillow'),
        'random_seed':20260922,
        'reproduction_command':'python scripts/run_all.py',
        'code_and_docs_sha256':{str(p.relative_to(ROOT)):sha256(p) for p in files},
        'results_sha256':{str(p.relative_to(ROOT)):sha256(p) for p in outputs},
        'processed_data_sha256':{str(p.relative_to(ROOT)):sha256(p) for p in processed},
        'sources_manifest_sha256':sha256(ROOT/'data/sources.json'),
        'goal_status':'Research results persisted; full decipherment unresolved.'})

if __name__=='__main__':
    main()
