# generate_outputs.py

import yaml, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
with open(ROOT/"data"/"assumptions.yaml") as f:
    data = yaml.safe_load(f)

totals = {t: sum(c.values()) for t, c in data["tiers"].items()}
default_tier = "baseline"

dashboard = ROOT/"dashboard"
dashboard.mkdir(exist_ok=True)
out = {"tiers": data["tiers"], "totals": totals, "default": default_tier}
with open(dashboard/"metrics.json","w") as f:
    json.dump(out, f, indent=2)
print("✓ metrics.json generated")
