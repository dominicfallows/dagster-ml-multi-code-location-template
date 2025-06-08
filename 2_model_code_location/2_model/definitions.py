# Dagster definitions for the model code location
from dagster import Definitions
from .assets import train_model_asset, vocab_from_train_data

definitions = Definitions(assets=[train_model_asset, vocab_from_train_data])
