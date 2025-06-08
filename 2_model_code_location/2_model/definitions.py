# Dagster definitions for the model code location
from dagster import Definitions
from .assets import train_model_asset

definitions = Definitions(assets=[train_model_asset])
