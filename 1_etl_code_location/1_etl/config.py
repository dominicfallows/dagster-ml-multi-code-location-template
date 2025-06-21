import os
import yaml

# Load ETL job config from YAML
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.yaml")
with open(CONFIG_PATH, "r") as f:
    _config = yaml.safe_load(f)

# Expose ops config
ops = _config.get("ops", {})
