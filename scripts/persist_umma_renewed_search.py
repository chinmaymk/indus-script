"""Pin the bounded renewed Umma search and recovered published figure."""
import json
from common import ROOT, sha256, write_json


def pin(path):
    p = ROOT / path
    return {'path': path, 'bytes': p.stat().st_size, 'sha256': sha256(p)}


def main():
    captures = sorted((ROOT / 'data/raw').glob('umma-anchor-renewed-*.json'))
    sources = [{**pin(str(p.relative_to(ROOT))),
                'kind': 'serialized_web_tool_response_capture', 'url': None,
                'not_original_HTTP_body': True} for p in captures
               if not p.name.endswith('.headers.json')]
    fetch = json.loads((ROOT / 'data/processed/fetch_umma-anchor-renewed-figure_webp.json').read_text())
    assert fetch['http_status'] == 200 and fetch['response_complete']
    sources.append({**{k: v for k, v in fetch.items() if k != 'header_artifact'},
                    'kind': 'published_review_figure_HTTP_body',
                    'content_review_status': 'visually_inspected_figure_D_and_E_distinct'})
    sources.append({**fetch['header_artifact'], 'url': fetch['url']})
    write_json('data/processed/umma_renewed_new_sources.json', {'sources': sources})
    write_json('data/processed/umma_renewed_search.json', {
        'date': '2026-09-28',
        'queries': ['"TJ17-PRO-S56"', '"978-80-89704-05-7" pdf',
                    'SAHI Tell Jokha 2017 report seal 59 Hulinek',
                    'SAHI Tell Jokha 2017 filetype:pdf', 'Tell Jokha Harappan seal S56'],
        'queries_total': 5,
        'outcomes': {
            'review_figure_recovered_and_visually_inspected': True,
            'original_2017_report_page_recovered': False,
            'exact_TJ17_PRO_S56_id_primary_authenticated': False,
            'known_referent_or_parallel_text_join_authenticated': False,
            'semantic_or_phonetic_values_assigned': 0,
        },
        'figure': {'url': fetch['url'], 'panel': 'D',
                   'caption_reference': 'SAHI Tell Jokha report p59 fig6.61',
                   'source_class': 'published secondary reproduction credited to SAHI',
                   'panel_E': 'older Ashmolean object; not merged with D',
                   'no_rotation_mirroring_or_transcription_assigned': True},
        'library_leads': [
            {'url': 'https://sclib.svkk.sk/sck01test/Record/000596329',
             'source_status': 'indexed official catalogue result; direct web open Internal Error',
             'ISBN': '978-80-89704-05-7', 'call_number': 'V.237993',
             'availability': 'physical copy and scan-request service reported by indexed result; no request made',
             'pagination': '79 numbered plus190 unnumbered pages; not verified from copy'},
            {'url': 'https://www.unige.ch/lettres/antic/download_file/view/1214/589',
             'source_status': 'official2page PDF extracted via web tool',
             'actual_content': '6July2019 conference programme; no object catalogue or figure',
             'recent_search_date_is_not_publication_date': True}],
        'limitations': [
            'Duplicate June2026 Reddit posts are one unverified discovery lead, not two independent confirmations.',
            'Published panel orientation is observable, but seal-versus-impression and original report orientation are unresolved.',
            'A readable cuneiform tablet from the same city is not a physical or semantic join.',
            'No outreach, request submission, login or restriction bypass.'],
        'evidence_pins': [pin(s['path']) for s in sources] + [
            pin('docs/UMMA_ANCHOR_AUDIT.md'), pin('data/processed/umma_anchor_review.json')],
    })
    print(f'Umma renewed search: 5 queries, {len(sources)} retained source artifacts, figure recovered.')


if __name__ == '__main__':
    main()
