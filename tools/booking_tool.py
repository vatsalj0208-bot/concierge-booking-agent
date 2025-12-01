import json
from pathlib import Path
from datetime import datetime
from tools.logger import Logger
BOOK=Path(__file__).resolve().parents[1]/'data'/'bookings.json'
logger=Logger()
def _read():
    with open(BOOK) as f: return json.load(f)
def _write(d):
    with open(BOOK,'w') as f: json.dump(d,f,indent=2)
def make_booking(name,kind,time):
    d=_read()
    bid=len(d)+1
    entry={'id':bid,'name':name,'type':kind,'time':time,'created_at':datetime.utcnow().isoformat()+'Z'}
    d.append(entry); _write(d)
    logger.log({'tool':'booking','entry':entry})
    return entry
