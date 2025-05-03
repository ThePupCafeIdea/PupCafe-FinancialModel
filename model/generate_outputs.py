import yaml, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]

# --- Load YAML tiers ---
with open(ROOT / "data" / "assumptions.yaml") as f:
    data = yaml.safe_load(f)

# Calculate a total for each tier
launch_costs = {
    tier: sum(items.values()) for tier, items in data["tiers"].items()
}

# Default tier to show first
default_tier = "baseline"

# Write JSON for the dashboard
output = {
    "tiers": data["tiers"],
    "totals": launch_costs,
    "default": default_tier
}

dashboard_dir = ROOT / "dashboard"
dashboard_dir.mkdir(exist_ok=True)

with open(dashboard_dir / "metrics.json", "w") as f:
    json.dump(output, f, indent=2)

print("✓ metrics.json generated (YAML only)")
