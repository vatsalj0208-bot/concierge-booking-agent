import json
from pathlib import Path
DATA = Path(__file__).resolve().parents[1]/'data'/'availability.json'
def _load():
    with open(DATA) as f: return json.load(f)
def search_availability(kind:str):
    return _load().get(kind.lower(),[])
