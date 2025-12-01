import json
from pathlib import Path
MEM=Path(__file__).resolve().parents[1]/'data'/'memory.json'
class MemoryTool:
    def _read(self):
        with open(MEM) as f: return json.load(f)
    def _write(self,d):
        with open(MEM,'w') as f: json.dump(d,f,indent=2)
    def set(self,k,v):
        d=self._read(); d[k]=v; self._write(d)
    def get(self,k,default=None):
        return self._read().get(k,default)
