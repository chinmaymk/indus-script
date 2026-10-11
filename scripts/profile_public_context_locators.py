"""One frozen metadata-only locator pass; no authenticated global join or sign test."""
from collections import Counter, defaultdict
from pathlib import Path
import csv
import hashlib
import json
from profile_public_context_tables import artifact_key, normalized, present, numeric

ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = ROOT / 'data/processed/public_context_locator_protocol_v1.json'
OUTPUT = ROOT / 'results/public_context_locators_v1.json'
LIPI_COLUMNS = ('id', 'cisi', 'site', 'excavation-idno')
TABLE_COLUMNS = ('no', 'field_no', 'area', 'block', 'house', 'room', 'street', 'level_ft', 'pdf_page')


def locate(table, lipi):
    keys, fields = defaultdict(list), defaultdict(list)
    for index, row in enumerate(table):
        if present(row['field_no']):
            fields[normalized(row['field_no'])].append(index)
        if present(row['field_no']) and present(row['no']):
            keys[normalized(row['field_no']) + normalized(row['no'])].append(index)
    lipi_keys, artifact_fields, artifact_sites = defaultdict(list), defaultdict(set), defaultdict(set)
    for row in lipi:
        artifact = artifact_key(row)
        if artifact is not None:
            artifact_sites[artifact].add(row['site'])
            if present(row['excavation-idno']):
                artifact_fields[artifact].add(normalized(row['excavation-idno']))
        if present(row['excavation-idno']):
            lipi_keys[normalized(row['excavation-idno'])].append(row)
    candidates, excluded = [], []
    for index, row in enumerate(table):
        reasons = []
        key = (normalized(row['field_no']) + normalized(row['no'])
               if present(row['field_no']) and present(row['no']) else None)
        witnesses = lipi_keys.get(key, []) if key is not None else []
        artifacts = {artifact_key(r) for r in witnesses}
        if key is None:
            reasons.append('missing_table_key_component')
        else:
            if len(keys[key]) != 1:
                reasons.append('concatenation_collision_or_duplicate_table_key')
            if len(fields[normalized(row['field_no'])]) != 1:
                reasons.append('nonunique_table_field_key')
        if not witnesses:
            reasons.append('no_literal_lipi_locator')
        elif None in artifacts or len(artifacts) != 1:
            reasons.append('missing_or_multiple_lipi_artifact_keys')
        else:
            artifact = next(iter(artifacts))
            if len(artifact_fields[artifact]) != 1:
                reasons.append('artifact_has_inconsistent_fields')
            if artifact_sites[artifact] != {'Mohenjo-daro'}:
                reasons.append('artifact_site_not_exclusively_mohenjo_daro')
        record = dict(table_index=index, candidate_composite_key=key, table_metadata=row,
                      lipi_witnesses=witnesses, artifact_keys=sorted(a for a in artifacts if a is not None))
        if reasons:
            excluded.append({**record, 'reasons':reasons})
        else:
            candidates.append({**record, 'status':'provisional_locator_only_not_authenticated_identity'})
    tuples = defaultdict(list)
    for record in candidates:
        row = record['table_metadata']
        complete = all(present(row[k]) for k in ('area', 'block', 'house', 'room', 'level_ft')) and numeric(row['level_ft'])
        record['complete_raw_locus_depth_tuple'] = complete
        if complete:
            # Preserve literal signed depth, area and every locus component.
            key = tuple(row[k] for k in ('area', 'block', 'house', 'room', 'level_ft'))
            tuples[key].append(record['artifact_keys'][0])
    summary = dict(table_rows=len(table), provisional_locators=len(candidates), excluded_table_rows=len(excluded),
                   distinct_provisional_artifact_keys=len({r['artifact_keys'][0] for r in candidates}),
                   with_complete_raw_locus_depth_tuple=sum(r['complete_raw_locus_depth_tuple'] for r in candidates),
                   distinct_complete_raw_tuples=len(tuples),
                   repeated_complete_raw_tuples=sum(len(set(v)) >= 2 for v in tuples.values()),
                   exclusion_reason_counts=dict(sorted(Counter(reason for r in excluded for reason in r['reasons']).items())))
    return dict(summary=summary, candidates=candidates, exclusions=excluded,
                raw_tuple_coverage=[dict(raw_tuple=list(k), provisional_artifact_keys=sorted(set(v)),
                                        distinct_provisional_artifact_keys=len(set(v))) for k,v in sorted(tuples.items())],
                missing_lipi_fields=[r for r in lipi if r['site']=='Mohenjo-daro' and not present(r['excavation-idno'])],
                limit='Coverage diagnostics only. Raw tuple equality does not establish deposits, independence, contemporaneity, original use, semantic values or validated global parsing.')


def read_projected(path, columns):
    with path.open(newline='') as stream:
        return [{k:r[k] for k in columns} for r in csv.DictReader(stream)]


def main():
    if OUTPUT.exists():
        raise FileExistsError('Frozen locator result already exists')
    protocol = json.loads(PROTOCOL.read_text())
    for pin in protocol['source_pins']:
        if hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest() != pin['sha256']:
            raise ValueError('Frozen source changed: '+pin['path'])
    result = locate(read_projected(ROOT/'data/raw/public-context-oct11-mackay-seal-table.csv', TABLE_COLUMNS),
                    read_projected(ROOT/'data/raw/lipi_inscriptions.csv', LIPI_COLUMNS))
    result['protocol'] = dict(path=str(PROTOCOL.relative_to(ROOT)), sha256=hashlib.sha256(PROTOCOL.read_bytes()).hexdigest())
    result['implementation_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result['source_pins'] = protocol['source_pins']
    result['status'] = 'complete_one_pass_stop_before_primary_pilot_or_contextual_use'
    OUTPUT.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['summary'],indent=2))


if __name__ == '__main__':
    main()
