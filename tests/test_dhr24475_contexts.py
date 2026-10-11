import sys,unittest,itertools
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from screen_dhr24475_contexts import parse_closed_slots,exact_relations,possible_relations

class DhrContextTests(unittest.TestCase):
 def test_exhaustive_singleton_neighborhood(self):
  target=('001','002','003','001')
  for seq in itertools.product(('001','002','003'),repeat=4):
   text='+'+'-'.join(seq)+'+'
   expected=[] if sum(a!=b for a,b in zip(seq,target))>1 else ['exact_duplicate'] if seq==target else ['one_position_'+str(next(i for i,(a,b) in enumerate(zip(seq,target)) if a!=b))]
   self.assertEqual(exact_relations(parse_closed_slots(text),target),expected)
 def test_ambiguity_is_not_certain(self):
  slots=parse_closed_slots('+391/390-002-365-550+')
  self.assertEqual(exact_relations(slots),[])
  self.assertEqual(possible_relations(slots),['exact_duplicate_compatible','one_position_0_compatible'])
 def test_no_reversal_insertion_or_internal_substring(self):
  for text in ['+550-365-002-391+','+391-002-365-550-001+','+002-365-550+','+001-391-002-365-550+']:
   self.assertEqual(exact_relations(parse_closed_slots(text)),[])
 def test_damage_doubt_linebreak_and_unknown_not_clean_slots(self):
  for text in [']391-002-365-550+','+391-002-365-550[','+391-002-365-*550+','+391-002-365-000+','+391-002-365-999+','+391-002\n365-550+','+391-002+365-550+','+391-002-365-55+']:
   self.assertIsNone(parse_closed_slots(text),text)
 def test_multiple_alternatives_do_not_force_single_change(self):
  slots=parse_closed_slots('+390/389-001/003-365-550+')
  self.assertEqual(possible_relations(slots),[])
 def test_slots_retain_zero_padding(self):
  self.assertEqual(parse_closed_slots('+391-002-365-550+')[1],frozenset({'002'}))

if __name__=='__main__':unittest.main()
