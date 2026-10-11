"""Retrieve finite primary narrative pages; fetch helper preserves each response."""
from pathlib import Path
import subprocess,sys
R=Path(__file__).resolve().parents[1]
for page in [40,48,49,50,56,58]:
 leaf=page+20
 name=f'chanhu-deposit-leaf{leaf}.jpg'
 if (R/'data/raw'/name).exists():continue
 subprocess.run([sys.executable,str(R/'scripts/fetch_preserved_source.py'),f'https://archive.org/download/in.gov.ignca.27263/page/n{leaf}.jpg',name],check=True)
