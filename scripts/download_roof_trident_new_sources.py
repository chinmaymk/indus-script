"""Bounded public primary-source retrieval; actual response bytes stay in data/raw."""
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError
import hashlib,json,datetime
ROOT=Path(__file__).resolve().parents[1]
SOURCES=[
('roof_trident_new_dholavira_report_candidate.pdf','https://asi.nic.in/pdf/dholavira_excavation_report.pdf','official_report_candidate'),
('roof_trident_new_nausharo_jarrige1996.pdf','https://www.persee.fr/docAsPDF/crai_0065-0536_1996_num_140_3_15636.pdf','primary_excavator_article'),
('roof_trident_new_archive_dholavira.json','https://archive.org/advancedsearch.php?q=title%3A%28Dholavira%29&fl%5B%5D=identifier&fl%5B%5D=title&rows=50&output=json','archive_search_metadata'),
('roof_trident_new_dholavira_archive_metadata.json','https://archive.org/metadata/dholavirareportpreliminaryjan2015_860_K','archive_item_metadata'),
('roof_trident_new_archive_cisi32.json','https://archive.org/advancedsearch.php?q=title%3A%28Corpus+Indus+Seals%29&fl%5B%5D=identifier&fl%5B%5D=title&rows=50&output=json','archive_search_metadata'),
('roof_trident_new_dholavira_2015.pdf','https://archive.org/download/dholavirareportpreliminaryjan2015_860_K/Dholavira%20Report%20%28preliminary%2C%20Jan%202015%29.pdf','third_party_archive_copy_of_primary_report_pending_visual_authentication'),
('roof_trident_new_dholavira_2015_replica.pdf','https://ia801906.us.archive.org/19/items/dholavirareportpreliminaryjan2015_860_K/Dholavira%20Report%20%28preliminary%2C%20Jan%202015%29.pdf','archive_metadata_advertised_replica_after_download500'),
('roof_trident_new_DHR24475_museum.jpg','http://museumsofindia.gov.in:81/cdn/portal_record/%5Bnat_del%5D/nat_del-DHR-24475-18639/nat_del-DHR-24475-18639_01_l.jpg','official_museum_image_from_retained_exact_record'),
]
def main():
 ledger=ROOT/'data/processed/roof_trident_new_download_attempts.json'
 results=json.loads(ledger.read_text()) if ledger.exists() else []
 for name,url,kind in SOURCES:
  if any(r['url']==url for r in results): continue
  row={'url':url,'planned_path':'data/raw/'+name,'kind':kind,'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
  try:
   response=urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0 (research source retrieval)'}),timeout=45)
   data=response.read(); row.update(status=response.status,resolved_url=response.url,content_type=response.headers.get('Content-Type'))
   if name.endswith('.pdf') and not data.startswith(b'%PDF'):
    name=name[:-4]+'_nonpdf.html'; row['not_a_pdf']=True
   dest=ROOT/'data/raw'/name; dest.write_bytes(data)
   row.update(path=str(dest.relative_to(ROOT)),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
  except HTTPError as exc:
   row['error']=str(exc); data=exc.read()
   if data:
    dest=ROOT/'data/raw'/(Path(name).stem+'_error_response.bin'); dest.write_bytes(data)
    row.update(path=str(dest.relative_to(ROOT)),bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),kind='http_error_response',status=exc.code)
  except Exception as exc:
   row['error']=str(exc)
  results.append(row)
 ledger.write_text(json.dumps(results,indent=2)+'\n')
 print(json.dumps(results,indent=2))
if __name__=='__main__':main()
