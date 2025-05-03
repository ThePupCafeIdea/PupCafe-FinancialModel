import yaml, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
data = yaml.safe_load(open(ROOT/'data'/'assumptions.yaml'))
(ROOT/'dashboard').mkdir(exist_ok=True)
json.dump(data, open(ROOT/'dashboard'/'metrics.json','w'), indent=2)
print("✓ metrics.json generated")
