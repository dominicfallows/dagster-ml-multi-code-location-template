# Dagster definitions for the deploy code location
from dagster import Definitions
from .assets import deploy_model_asset

definitions = Definitions(assets=[deploy_model_asset])
