import json
from pathlib import Path
from datetime import datetime
LOG=Path(__file__).resolve().parents[1]/'logs.txt'
class Logger:
    def log(self,obj):
        entry={'timestamp':datetime.utcnow().isoformat()+'Z',**obj}
        with open(LOG,'a') as f: f.write(json.dumps(entry)+'\n')
