"""Enumerate existing local W391 rows and persist bounded identity dispositions.

No translation columns are read into output. Dispositions are explicit manual
source-review findings; this is not a automatic W-to-M conversion or corpus patch.
"""
from pathlib import Path
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def main():
    fields = ['id', 'cisi', 'excavation-idno', 'site', 'type', 'preservation', 'complete', 'condition', 'text', 'dir.']
    with (ROOT / 'data/raw/lipi_inscriptions.csv').open(newline='') as f:
        selected = [{key: row[key] for key in fields} for row in csv.DictReader(f)
                    if re.search(r'(?<!\d)391(?!\d)', row['text'])]
    native = [json.loads(line) for line in (ROOT / 'data/processed/m77_candidate_records.jsonl').read_text().splitlines()]
    target_native = [r for r in native if any(t['sign'] == 'M163' for t in r['tokens'])]
    assert {r['source_reference'] for r in target_native} == {'1051','1397','2119','2925','8054'}
    by_ref = {r['source_reference']: r for r in native}
    decisions = {
      '1911.1': ('8054', 'old_native_target_documentary_join', 'K-45 = KLB1 19360 = ASI68.1.51. CISI printed374/PDF410 and M77 Appendix printed827/PDF836 give the same field and registration. Finnish7120 is a separate catalogue number.', 'Raw preservation fragment coexists with complete=Y; do not decide inscription completeness from either field alone. Native target field has no exported doubt/loss, but no new physical roof reading here.'),
      '2221.1': ('2119', 'old_native_target_candidate_join', 'Secondary DK10551119 plausibly combines DK10551 and FEM119. M77 Appendix printed818/PDF827 explicitly maps FEM119 to2119. The original field10551-to-item119 row was not authenticated here; modern M1892 alias remains qualified.', 'Raw preservation fragment and complete=Y conflict at object-label level; alternative token706/821 retained. Native2119 has source_doc_count2 and strict=false; identical tail to other tools cannot authenticate identity.'),
      '2362.1': ('2925', 'old_native_target_documentary_join', 'Raw CXXVI:5 joins existing M77 Appendix2925=CXXVI5 and original Mackay table printed489, field7535. Later Pettersson7835 remains unresolved; no silent repair.', 'Native first field contains doubtfulM098. W string is six tokens versus seven normalized M77 codes; no global one-token equivalence or complete-field agreement is claimed.'),
      '2368.1': (None, 'unjoined_historical_tool_candidate', 'Raw DK7854/CXXXI37 retained literally. Prior plate audit only tentatively compared photograph37 with the small axe; no authenticated individual photo-to-field bridge. Do not assign2924,2925 or2923 from similar text.', 'Raw complete=Y does not authenticate original field completeness or W391 roof. Existing M77 Appendix selected tool list has no explicit CXXXI37 row; bounded missing join is not proof of corpus omission.'),
      '2370.1': ('2923', 'old_native_object_target_not_recoverable_in_M77', 'CXXVI2 is explicitly M77:2923, conventionally DK7856, with original table digit blur retained. This is the already studied broken tang, not another object.', 'W export suppliesW391 where native first field begins LOSS, followed byM252 M261 M134 doubtfulM098 M391 doubtfulM391. Primary printed85/PDF96 shows the initial hatched span. Cannot insertM163 from the similar2925 inscription. Raw preservation complete/complete=Y differs from original fragmentary tool condition.'),
      '2568.1': ('1051', 'old_native_target_documentary_join', 'Marshall volumeII printed402/PDF53 row51 is HR4945. M77 Appendix printed818/PDF827 maps MIC51 to1051. Modern M40 alias was not separately checked in CISI metadata.', 'Native field is strict and undoubted. This is additional cross-catalogue documentation for a known native target, not an additional target artifact.'),
      '3399.1': ('1397', 'old_native_target_documentary_join', 'Marshall volumeII printed404/PDF55 row397 is VS3227. M77 Appendix printed818/PDF827 maps MIC397 to1397. Modern M1014 alias remains secondary.', 'Raw fragment, complete=?, and open text boundary agree with a need for caution; native field has LOSS and doubtfulM341. Cannot enter a complete-undoubted test.'),
      '3680.1': (None, 'unjoined_tag_candidate', 'M1384 has no excavation identifier in raw row. Its shared tail does not join it to FEM119,2925,2923 or another tool. Preserve distinct source row without declaring distinct ancient artifact.', 'Raw typeTAG:L, complete=Y and poor condition are source labels; no primary object or original roof state authenticated.'),
      '4196.1': (None, 'external_source_candidate_pending_other_review', 'Raw DHR-24475 from Dholavira is an additional W-coded candidate outside the five identified nativeM163 target references. No native-M77 identity bridge or photograph assignment made here.', 'Primary image and object identity delegated to separate source review. A new candidate to this native-target selection is not an authenticated newM163 token or independently new physical object.'),
      '5355.1': (None, 'external_source_candidate_pending_other_review', 'Raw Ns-53 / NS91.02.17.01 from Nausharo is an additional W-coded candidate outside the five identified nativeM163 target references. No native-M77 identity bridge or photograph assignment made here.', 'Primary image and object identity delegated to separate source review. Do not infer discovery date, semantic novelty or physical independence merely from the identifier or site.')
    }
    assert {r['id'] for r in selected} == set(decisions)
    ledger=[]
    for raw in selected:
        ref,status,basis,limit=decisions[raw['id']]
        row={'raw':raw,'candidate_target':'W391','native_reference':ref,'status':status,
             'identity_basis':basis,'limits':limit,
             'is_extra_raw_candidate_beyond_five_native_target_references': ref not in {'1051','1397','2119','2925','8054'},
             'new_native_M163_attestation_authenticated':False,
             'new_physical_artifact_authenticated_by_this_audit':False,
             'modern_alias_separately_authenticated':raw['id']=='1911.1'}
        if ref:
            n=by_ref[ref]
            row['native_export']={k:n[k] for k in ['id','source_reference','source_doc_count','source_direction_code','strict_candidate','tokens']}
            row['native_object_presence']='present; candidate identity qualification applies' if raw['id']=='2221.1' else 'present via documented locator'
        else:
            row['native_object_presence']='unresolved; no global absence claim'
        ledger.append(row)
    sources=['data/raw/lipi_inscriptions.csv','data/processed/m77_candidate_records.jsonl','data/processed/catalogue_features.json',
      'data/processed/arch_extension_catalogue_review.json','data/processed/bronze2923_identity_review.json',
      'data/processed/metal_original_records.json','data/processed/metal_plate_audit.json',
      'data/raw/mahadevan_1977_text.pdf','data/raw/cisi_76884.pdf','data/raw/stone1471_marshall1931_volume2_text.pdf',
      'data/raw/metal_original_mackay18225_djvu.txt','data/raw/metal_original_mackay_leaf511.jpg',
      'results/primary_pages/chain-artifact-m77-827.png','results/primary_pages/roof-m092-artifact-m77-836.png',
      'results/primary_pages/metal-kalibangan-data-410.png','results/primary_pages/comb-tablet-mic-53.png',
      'results/primary_pages/roof-trident-marshall-55.png','results/primary_pages/orientation-text-96.png',
      'results/primary_pages/arch-extension-2925-detail.png','results/primary_pages/metal-original-table-rows.png',
      'results/roof-trident-marshall_extraction.json','scripts/audit_roof_trident_candidates.py']
    pins=[]
    for path in sources:
        content=(ROOT/path).read_bytes();pins.append({'path':path,'bytes':len(content),'sha256':hashlib.sha256(content).hexdigest()})
    feature=next(x for x in json.loads((ROOT/'data/processed/catalogue_features.json').read_text()) if x['id']=='P089')
    output={'schema_version':1,'scope':'Complete local rawW391 row enumeration and bounded identity/source-selection audit; no conversion or semantic assignment.',
      'feature_candidate':feature,'feature_scope':'P089 listsW391 andM163 as candidate cross-catalogue members; not a universal identity rule. W391 andM391 belong to different schemes.',
      'raw_target_row_count':len(selected),'native_M163_reference_set':sorted(r['source_reference'] for r in target_native),
      'candidate_ledger':ledger,
      'summary':{'documented_old_native_target_joins':4,'candidate_old_native_target_join':1,'known_native_object_with_unrecoverable_target':1,
                 'unjoined_historical_candidates':2,'additional_external_source_candidates_pending_primary_review':2,
                 'new_native_M163_attestations_authenticated':0,'new_physical_artifacts_authenticated_by_this_audit':0},
      'newness_definitions':{'raw_source_row':'Ten existing raw W391 rows are enumerated; no new download or new raw record is created.',
                            'native_target_export':'Five selected target references already containM163. Four documentary joins and one qualified candidate account for their apparent W391 counterparts.',
                            'additional_candidate':'Five other W rows are extra candidates relative to that target set; one already maps to native2923 with LOSS, two historical joins remain unresolved, two external-source rows await separate review.',
                            'new_physical_artifact':'Not established for any candidate merely from source-row counts, shared/different text, or lack of native target mapping.'},
      'attempts':[{'attempt':'Delimiter-aware CSV scan for391','result':'Ten rows; exact token scan independently returned same ten. Translation columns excluded from saved fields.'},
                  {'attempt':'Scan native candidate records forM163 and inspect selected2923','result':'Exactly1051,1397,2119,2925,8054. Separate2923 starts unknown span with two doubtful positions.'},
                  {'attempt':'Review existing original metal/arch ledgers and primary Texts85/PDF96','result':'2925target retained with other-sign doubt;2923initial target not recoverable. Primary field7535/later7835 disagreement preserved.'},
                  {'attempt':'Inspect M77 Appendix818/PDF827 and827/PDF836, CISI374/PDF410, Marshall402/PDF53','result':'Verified old publication mapping rules, K45/19360/8054 and HR4945/MIC51/1051 documentary chains.'},
                  {'attempt':'Render retained Marshall volumeII PDF55 with roof-trident-marshall prefix','result':'Printed404 row397 visibly VS3227, giving qualified M1014/MIC397/1397 chain.'},
                  {'attempt':'Search retained Mackay OCR for7854 and10551','result':'No reliable exact hit or new individual bridge. OCR weakness is not absence evidence; no download or speculative repair.'}],
      'new_downloads':[],'corpus_edits':[],'established_semantic_values':0,'established_phonetic_values':0,'evidence_files':pins}
    (ROOT/'data/processed/roof_trident_candidate_audit.json').write_text(json.dumps(output,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(output['summary'],indent=2))


if __name__=='__main__':
    main()
