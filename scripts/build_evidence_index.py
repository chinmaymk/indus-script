"""Join all-sign evidence without turning provisional links into sign identities."""
from collections import defaultdict
import csv
import json
from common import ROOT, sha256, write_json, write_csv


def build_index(dossiers, families, features, copper):
    expected = {f'M{i:03d}' for i in range(1, 418)}
    by_sign = {r['sign']: r for r in dossiers}
    family_by_sign = {r['sign']: r for r in families}
    if len(dossiers) != 417 or set(by_sign) != expected:
        raise ValueError('Dossier coverage must be exactly M001–M417, once each')
    if len(families) != 417 or set(family_by_sign) != expected:
        raise ValueError('Family coverage must be exactly M001–M417, once each')
    links = defaultdict(list)
    mapped_w = set()
    candidate_w = set(copper['all_conditions']['singleton_to_source_labels'])
    for f in features:
        for w in f.get('wells_graphemes', []):
            if w not in candidate_w:
                continue
            members = f.get('mahadevan_graphemes', [])
            if members:
                mapped_w.add(w)
            for m in members:
                if m not in expected:
                    raise ValueError(f'Out-of-inventory M identifier: {m}')
                links[m].append({'W': w, 'via_P': f['id'],
                    'M_candidates_in_source_entry': members,
                    'W_members_in_source_entry': f['wells_graphemes'],
                    'source_feature_path': f['source_path'],
                    'motif_labels_all_conditions': copper['all_conditions']['singleton_to_source_labels'][w],
                    'motif_labels_good_fair_only': copper['good_fair_only']['singleton_to_source_labels'].get(w, []),
                    'relation': 'catalogue membership only; does not identify this M sign with this W sign'})
    result = []
    for sign in sorted(expected):
        d, f = by_sign[sign], family_by_sign[sign]
        result.append({'sign': sign, 'image': d['image'], 'image_sha256': d['sha256'],
            'primary_M77': {'solus': int(d['m77_solus']), 'initial': int(d['m77_initial']),
                'medial': int(d['m77_medial']), 'final': int(d['m77_final']),
                'total': int(d['m77_total']), 'pdf_page': int(d['m77_primary_pdf_page']),
                'description': d['m77_distributional_description']},
            'catalogue_mapping_status': d['mapping_status'],
            'candidate_W_ids': d['candidate_wells_ids'].split(';') if d['candidate_wells_ids'] else [],
            'family_test': {'coverage': f['coverage'],
                'supported_P_families': f['supported_families'].split(';') if f['supported_families'] else [],
                'inference': 'variant-context evidence, not proof of allography or meaning'},
            'conditional_copper_links': links[sign],
            'semantic_value': None, 'phonetic_value': None,
            'reading_status': 'undetermined'})
    return result, sorted(candidate_w - mapped_w)


def attach_substitution_evidence(rows, features, signs):
    """Attach every candidate path, never project W identity through a many-way entry."""
    by_m={r['sign']:r for r in rows}
    mapped=set()
    for r in rows:
        r['conditional_substitution_links']=[]
    for entry in features:
        members=entry.get('mahadevan_graphemes',[])
        for w in entry.get('wells_graphemes',[]):
            if w not in signs: continue
            for m in members:
                if m not in by_m: raise ValueError(f'Unknown M member {m}')
                mapped.add(w)
                by_m[m]['conditional_substitution_links'].append({
                    'W':w,'via_P':entry['id'],
                    'M_candidates_in_source_entry':members,
                    'W_members_in_source_entry':entry['wells_graphemes'],
                    'evidence':signs[w],
                    'relation':'Catalogue membership only; substitution is not allography, synonymy or an individual M-W identity'})
    return sorted(set(signs)-mapped)


def attach_candidate_m77_profiles(rows, profiles):
    """Attach qualified secondary counts without upgrading their source or meaning."""
    by_sign = {p['sign']: p for p in profiles}
    if len(profiles) != len(rows) or len(by_sign) != len(rows) or set(by_sign) != {r['sign'] for r in rows}:
        raise ValueError('Candidate M77 profile coverage must match all index signs')
    for r in rows:
        p = by_sign[r['sign']]
        if p['primary_table_total'] != r['primary_M77']['total']:
            raise ValueError('Primary-frequency join mismatch')
        if sum(p['strict_candidate_positions'].values()) != p['strict_candidate_occurrences']:
            raise ValueError('Candidate positional-count mismatch')
        r['candidate_M77_sequence_profile'] = {
            k: p[k] for k in ('all_export_occurrences_including_doubtful',
                             'strict_candidate_occurrences', 'strict_candidate_positions')}
        r['candidate_M77_sequence_profile']['status'] = 'Conditional secondary transcription; selected primary lines checked, full corpus not authenticated; no established reading'


def attach_tool_graphics(rows, review):
    """Keep object-specific graphical correspondences separate from sign readings."""
    by_sign = {r['sign']: r for r in rows}
    for r in rows:
        r['object_specific_tool_graphics'] = []
    for obj in review['objects']:
        mapped = {m['normalized_token_index']: m for m in obj['mapping']}
        assert len(mapped) == len(obj['mapping'])
        tokens = obj['normalized_tokens']
        assert all(0 <= i < len(tokens) and tokens[i] == m['code'] for i, m in mapped.items())
        assert [t for i, t in enumerate(tokens) if i not in mapped] == obj['residual_tokens']
        for i, sign in enumerate(tokens):
            if sign not in by_sign:
                raise ValueError('Out-of-inventory tool token')
            by_sign[sign]['object_specific_tool_graphics'].append({
                'reference': obj['m77_reference'], 'side': obj['side'], 'line': obj['line'],
                'complete_normalized_field': tokens, 'token_index': i,
                'role_in_review': 'graphic_correspondence' if i in mapped else 'uninterpreted_residual',
                'graphic_mapping': mapped.get(i),
                'scope': 'Published object-specific graphic alignment, not a universal unit, numeral, semantic or phonetic value',
                'source': 'data/processed/tool_sign_bridge_review.json'})


def attach_context_audits(rows, features, audits):
    """Expose all candidate catalogue paths without establishing M-W identities."""
    by_m={r['sign']:r for r in rows}
    for r in rows:r['conditional_context_audit_links']=[]
    for audit in audits:
        for m in audit.get('M_review_candidates',[]):
            if m not in by_m:raise ValueError('Out-of-inventory direct review candidate')
            by_m[m]['conditional_context_audit_links'].append({
                'audit':audit['id'],'source':audit['result'],'report':audit['report'],
                'W_candidates':audit['W_candidates'],'via_P':None,
                'M_candidates_in_source_entry':audit['M_review_candidates'],
                'W_members_in_source_entry':[], 'conclusion':audit['conclusion'],
                'scope':'Direct review linkage, including a disputed catalogue mapping; see report for artifact-specific evidence. No global sign merger or established reading.'})
        for feature in features:
            hits=sorted(set(feature.get('wells_graphemes',[])) & set(audit['W_candidates']))
            if not hits:continue
            for m in feature.get('mahadevan_graphemes',[]):
                if m not in by_m:raise ValueError('Out-of-inventory context-audit candidate')
                by_m[m]['conditional_context_audit_links'].append({
                    'audit':audit['id'],'source':audit['result'],'report':audit['report'],
                    'W_candidates':hits,'via_P':feature['id'],
                    'M_candidates_in_source_entry':feature['mahadevan_graphemes'],
                    'W_members_in_source_entry':feature['wells_graphemes'],
                    'conclusion':audit['conclusion'],
                    'scope':'Catalogue membership only; neither an exact M-W identity nor an established reading. Comparison targets need not occur on the named artifact.'})


def main():
    paths = {'dossiers': 'results/sign_dossiers_417.json',
             'families': 'results/sign_family_index_417.csv',
             'features': 'data/processed/catalogue_features.json',
             'copper': 'results/copper_bridge_audit.json',
             'substitution': 'results/substitution_network.json',
             'candidate_m77': 'results/m77_candidate_profiles_417.json',
             'reviewed_u': 'results/m77_u_recovery_audit.json',
             'reviewed_u_counterparts': 'results/m77_u_counterparts.json',
             'tool_graphics': 'data/processed/tool_sign_bridge_review.json',
             'tool_orientation': 'results/stroke_orientation_audit.json',
             'c40_layout': 'results/c40_layout_audit.json',
             'arch_extension': 'results/arch_mass_bound.json',
             'composite_expansion':'results/composite_expansion_audit.json',
             'context_audits':'data/processed/context_audit_links.json'}
    data = {k: (list(csv.DictReader((ROOT/p).open())) if p.endswith('.csv')
                else json.loads((ROOT/p).read_text())) for k,p in paths.items()}
    substitution=data.pop('substitution')
    candidate_m77=data.pop('candidate_m77')
    reviewed_u=data.pop('reviewed_u')
    reviewed_u_counterparts=data.pop('reviewed_u_counterparts')
    tool_graphics=data.pop('tool_graphics')
    tool_orientation=data.pop('tool_orientation')
    c40_layout=data.pop('c40_layout')
    arch_extension=data.pop('arch_extension')
    composite_expansion=data.pop('composite_expansion')
    context_audits=data.pop('context_audits')
    for audit in context_audits:
        result=json.loads((ROOT/audit['result']).read_text())
        assert result['established_semantic_values']==result['established_phonetic_values']==0
        paths['context_audit_'+audit['id']]=audit['result']
    composite_profiles={label:{r['sign']:r for r in branch['signs']}
                        for label,branch in composite_expansion['results'].items()}
    rows, unmapped = build_index(**data)
    attach_context_audits(rows,data['features'],context_audits)
    attach_candidate_m77_profiles(rows,candidate_m77)
    attach_tool_graphics(rows, tool_graphics)
    for r in rows:
        r['one_to_two_context_screen'] = {
            'profiles':{label:profiles[r['sign']] for label,profiles in composite_profiles.items()},
            'source':'results/composite_expansion_audit.json',
            'scope':'Exploratory exact-frame replacements in a selected secondary export; not established graphic composition or semantic equality'}
        r['arch_extension_primary_fields'] = [
            dict(line, source='data/processed/arch_extension_catalogue_review.json',
                 scope='Source-qualified catalogue field; overlapping earlier reviews, not independent frequency or meaning')
            for line in arch_extension['primary_fields'] if r['sign'] in line['tokens']]
        r['arch_extension_selected_occurrences'] = [
            dict(o, source='data/processed/arch_extension_catalogue_review.json')
            for o in arch_extension['selected_occurrences'] if o['sign']==r['sign']]
        r['primary_c40_fields'] = [
            {'reference':line['reference'], 'side':line['side'], 'line':line['line'],
             'complete_normalized_field':line['tokens'],
             'token_indices':[i for i,t in enumerate(line['tokens']) if t==r['sign']],
             'doubtful_token_indices':line['doubtful_token_indices'],
             'source':'data/processed/c40_catalogue_review.json',
             'scope':'Catalogue tokens, not physical linear order or numerical interpretation; fields remain separate'}
            for line in c40_layout['primary_c40_lines'] if r['sign'] in line['tokens']]
        r['selected_arch_primary_occurrences'] = [
            dict(o, source='data/processed/c40_catalogue_review.json')
            for o in c40_layout['selected_arch_occurrences'] if o['sign']==r['sign']]
        r['object_specific_orientation_reviews'] = [
            dict(obj, source='results/stroke_orientation_audit.json')
            for obj in tool_orientation['objects'] if r['sign'] in obj['normalized_tokens']]
        r['primary_reviewed_U_contexts'] = {
            'known_occurrences': reviewed_u_counterparts['corrected_U_context_sign_counts'].get(r['sign'],0),
            'scope': 'Known glyph occurrences in deduplicated primary M328-bearing lines; includes source doubt, excludes reviewer UNKNOWN; sign-selected corpus, not total frequency or meaning',
            'source': 'data/processed/m77_primary_reviewed_contexts.jsonl; scope=M328 concordance recovery',
            'historical_source': 'data/processed/m77_u_recovered_lines.jsonl',
            'later_corrections': 'data/processed/m77_u_3234_primary_review.json'}
        r['primary_reviewed_U_counterparts'] = {
            'known_occurrences': reviewed_u_counterparts['known_counterpart_sign_counts'].get(r['sign'],0),
            'scope': 'Known glyphs on other lines of references bearing exact long-stroke+U fields; includes source doubt, excludes UNKNOWN; overlaps with U contexts are possible, so do not sum these profiles as disjoint counts',
            'source': 'data/processed/m77_u_counterpart_lines.jsonl'}
    unmapped_substitution=attach_substitution_evidence(rows,data['features'],substitution['signs'])
    summary = {'M_rows': len(rows),
        'M_rows_with_conditional_context_audits':sum(bool(r['conditional_context_audit_links']) for r in rows),
        'M_rows_with_conditional_copper_links': sum(bool(r['conditional_copper_links']) for r in rows),
        'copper_W_codes_without_M_catalogue_link': unmapped,
        'M_rows_with_conditional_substitution_links':sum(bool(r['conditional_substitution_links']) for r in rows),
        'M_rows_with_candidate_substitution_edge':sum(any(x['evidence']['substitution_partner_count'] for x in r['conditional_substitution_links']) for r in rows),
        'substitution_W_codes_without_M_catalogue_link':unmapped_substitution,
        'M_rows_observed_in_candidate_M77_strict':sum(r['candidate_M77_sequence_profile']['strict_candidate_occurrences']>0 for r in rows),
        'M_rows_identified_in_primary_U_contexts':sum(r['primary_reviewed_U_contexts']['known_occurrences']>0 for r in rows),
        'M_rows_identified_in_primary_U_counterparts':sum(r['primary_reviewed_U_counterparts']['known_occurrences']>0 for r in rows),
        'M_rows_with_object_specific_tool_graphics': sum(bool(r['object_specific_tool_graphics']) for r in rows),
        'M_rows_with_object_specific_orientation_reviews': sum(bool(r['object_specific_orientation_reviews']) for r in rows),
        'M_rows_in_primary_c40_fields': sum(bool(r['primary_c40_fields']) for r in rows),
        'M_rows_with_selected_arch_primary_occurrences': sum(bool(r['selected_arch_primary_occurrences']) for r in rows),
        'M_rows_in_arch_extension_primary_fields': sum(bool(r['arch_extension_primary_fields']) for r in rows),
        'M_rows_with_arch_extension_selected_occurrences': sum(bool(r['arch_extension_selected_occurrences']) for r in rows),
        'M_rows_with_one_to_two_context_matches':sum(r['one_to_two_context_screen']['profiles']['complete_undoubted_export']['matches']>0 for r in rows),
        'established_semantic_values': 0, 'established_phonetic_values': 0,
        'primary_token_total': sum(r['primary_M77']['total'] for r in rows),
        'sources': {k: {'path': p, 'sha256': sha256(ROOT/p)} for k,p in paths.items()},
        'scope': 'Evidence coverage is not decipherment coverage. Conditional links are not readings; absence of a bridge is not evidence that a sign lacks meaning.'}
    write_json('results/sign_evidence_417.json', {'summary': summary, 'signs': rows})
    flat = []
    for r in rows:
        flat.append({'sign': r['sign'], 'primary_total': r['primary_M77']['total'],
            'conditional_context_audits':';'.join(sorted({a['audit'] for a in r['conditional_context_audit_links']})),
            'primary_description': r['primary_M77']['description'],
            'mapping_status': r['catalogue_mapping_status'],
            'family_coverage': r['family_test']['coverage'],
            'conditional_copper_W_candidates': ';'.join(sorted({x['W'] for x in r['conditional_copper_links']})),
            'conditional_copper_P_entries': ';'.join(sorted({x['via_P'] for x in r['conditional_copper_links']})),
            'conditional_substitution_W_candidates':';'.join(sorted({x['W'] for x in r['conditional_substitution_links']})),
            'candidate_M77_strict_occurrences':r['candidate_M77_sequence_profile']['strict_candidate_occurrences'],
            'primary_reviewed_U_context_occurrences':r['primary_reviewed_U_contexts']['known_occurrences'],
            'primary_reviewed_U_counterpart_occurrences':r['primary_reviewed_U_counterparts']['known_occurrences'],
            'object_specific_tool_references': ';'.join(sorted({x['reference'] for x in r['object_specific_tool_graphics']})),
            'object_specific_orientation_references': ';'.join(sorted({x['reference'] for x in r['object_specific_orientation_reviews']})),
            'primary_c40_fields': ';'.join(f"{x['reference']}.{x['side']}.{x['line']}" for x in r['primary_c40_fields']),
            'selected_arch_primary_occurrence_count': len(r['selected_arch_primary_occurrences']),
            'arch_extension_primary_fields': ';'.join(x['line_id'] for x in r['arch_extension_primary_fields']),
            'arch_extension_selected_occurrence_count':len(r['arch_extension_selected_occurrences']),
            'one_to_two_context_matches':r['one_to_two_context_screen']['profiles']['complete_undoubted_export']['matches'],
            'semantic_value': 'undetermined', 'phonetic_value': 'undetermined'})
    write_csv('results/sign_evidence_417.csv', flat)
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
