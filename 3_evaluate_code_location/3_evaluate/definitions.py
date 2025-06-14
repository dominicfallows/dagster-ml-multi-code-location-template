# Dagster definitions for the evaluate code location
from dagster import Definitions
from .assets import evaluate_model_asset, train_model_asset, split_asset

definitions = Definitions(
    assets=[evaluate_model_asset, train_model_asset, split_asset])
