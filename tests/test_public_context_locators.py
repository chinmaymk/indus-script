import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from profile_public_context_locators import locate


def table(field='DK 10799', no='3', **kw):
    return dict(field_no=field, no=no, area='DK', block='1', house='III', room='2',
                street='', level_ft='-8.0', pdf_page='45', **kw)


def lipi(field='DK107993', ident='a.1', cisi='M-1', site='Mohenjo-daro'):
    return {'excavation-idno':field, 'id':ident, 'cisi':cisi, 'site':site}


class LocatorTest(unittest.TestCase):
    def test_different_boundary_collision_is_rejected(self):
        r=locate([table('DK 10','23'),table('DK 102','3')],[lipi('DK1023')])
        self.assertEqual(r['summary']['provisional_locators'],0)
        self.assertTrue(all('concatenation_collision_or_duplicate_table_key' in x['reasons'] for x in r['exclusions']))

    def test_repeated_field_number_is_not_new_object(self):
        r=locate([table(no='3'),table(no='4')],[lipi(),lipi('DK107994',cisi='M-2')])
        self.assertEqual(r['summary']['provisional_locators'],0)
        self.assertTrue(all('nonunique_table_field_key' in x['reasons'] for x in r['exclusions']))

    def test_other_rows_can_invalidate_artifact(self):
        for extra, reason in [(lipi('DK20',ident='a.2'),'artifact_has_inconsistent_fields'),
                              (lipi(ident='a.2',site='Harappa'),'artifact_site_not_exclusively_mohenjo_daro'),
                              (lipi(cisi='M-2'),'missing_or_multiple_lipi_artifact_keys')]:
            with self.subTest(reason=reason):
                r=locate([table()],[lipi(),extra])
                self.assertIn(reason,r['exclusions'][0]['reasons'])

    def test_witnesses_do_not_inflate_objects_and_raw_datums_stay_separate(self):
        a=table(); b=table('SD 11','4'); b['area']='SD'
        r=locate([a,b],[lipi(),lipi(ident='a.2'),lipi('SD114',cisi='M-2')])
        self.assertEqual(r['summary']['distinct_provisional_artifact_keys'],2)
        self.assertEqual(r['summary']['distinct_complete_raw_tuples'],2)
        self.assertEqual(r['summary']['repeated_complete_raw_tuples'],0)
        self.assertEqual(len(r['candidates'][0]['lipi_witnesses']),2)

    def test_literal_strings_and_missing_context_are_preserved(self):
        a=table(); a['room']=''; a['level_ft']='Surface'
        r=locate([a],[lipi()])
        self.assertEqual(r['summary']['provisional_locators'],1)
        self.assertEqual(r['summary']['with_complete_raw_locus_depth_tuple'],0)
        for field in ['DK0107993','DK10799:3','DK107993x']:
            self.assertEqual(locate([table()],[lipi(field)])['summary']['provisional_locators'],0)


if __name__=='__main__': unittest.main()
