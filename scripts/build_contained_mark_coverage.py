"""Fixed follow-up of all contained-mark rows from the preceding table screen."""
from common import ROOT,sha256,write_json

def main():
    rows=[
        dict(serial=44,container_register='7856',contained_item='two goblet sherds: incised and seal-impressed',
             primary_text_reference=None,bridge_status='Shared register also describes an inscribed goblet in narrative; precise contained-item link unresolved.',
             rejected_promotions=['Illustrated CIV73 is only a similarity comparator','DK7856 is a different site and object'],
             review='data/processed/jar44_contained_goblets_review.json'),
        dict(serial=54,container_register='XII',contained_item='two-sided inscribed rectangular steatite seal',
             primary_text_reference=None,bridge_status='J630 candidate has matching square/depth/stratum but no explicit containment and a trench discrepancy.',
             candidate_chain=dict(field='J630',Vats='XCVI446',CISI='H890',M77='4446',accepted_as_contained_item=False),
             review='data/processed/jar54_contained_seal_review.json'),
        dict(serial=116,container_register='10252',contained_item='discoid faience sealing',
             primary_text_reference='M77:4671',bridge_status='Explicit contained-object publication reference and primary EH numbering rule.',
             surviving_normalized_field=['M089','M328'],counterpart=['LOSS'],
             jar_own_text_transcribed=False,
             review='data/processed/inscribed_jar_text_bridges.json'),
        dict(serial=156,container_register=None,contained_item='unicorn-seal fragment',
             primary_text_reference=None,bridge_status='No separate field number, plate or surviving text established.',
             review='data/processed/jar156_165_contained_marks_review.json'),
        dict(serial=165,container_register='7737',contained_item='one of three reported goblets, with four upright incisions',
             primary_text_reference=None,bridge_status='Stroke report without exact photograph or catalogue bridge; marks belong to goblet.',
             numeral_value=None,review='data/processed/jar156_165_contained_marks_review.json')]
    files=sorted({r['review'] for r in rows}|{'scripts/build_contained_mark_coverage.py','results/inscribed_jar_frame.json'})
    write_json('results/contained_mark_join_coverage.json',dict(scope='All five contained-mark/seal-fragment rows in the fixed prior table screen',
        row_serials=[r['serial'] for r in rows],rows=rows,rows_with_accepted_primary_text_bridge=1,
        rows_with_accepted_primary_text_bridge_before_this_followup=1,
        newly_established_contained_text_bridges=0,newly_established_own_jar_texts=0,
        rows_with_no_accepted_primary_text_bridge=4,ancient_distinct_vessel_count=None,
        semantic_values_assigned=0,phonetic_values_assigned=0,
        input_sha256={p:sha256(ROOT/p) for p in files}))
    print('Contained-mark coverage: all five selected rows followed; one prior accepted bridge, four unresolved; no new decoded text.')

if __name__=='__main__':main()
