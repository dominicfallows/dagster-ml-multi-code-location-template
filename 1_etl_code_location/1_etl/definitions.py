from dagster import Definitions, load_assets_from_modules
from shared.resources import input_files_resource, output_files_resource
import importlib
from .jobs import etl_job
from .schedules import etl_daily_schedule
from .sensors import etl_sensor

ingest_data = importlib.import_module(".1_ingest_data.assets", __package__)
tokenize_data = importlib.import_module(".2_tokenize_data.assets", __package__)
split_tokenized_data = importlib.import_module(
    ".3_split_tokenized_data.assets", __package__)
create_vocab_from_training_data = importlib.import_module(
    ".4_create_vocab_from_training_data.assets", __package__)
output_materialized_assets = importlib.import_module(
    ".5_output_materialized_assets.assets", __package__)

defs = Definitions(
    assets=load_assets_from_modules([
        ingest_data,
        tokenize_data,
        split_tokenized_data,
        create_vocab_from_training_data,
        output_materialized_assets
    ]),
    resources={
        "input_files_resource": input_files_resource,
        "output_files_resource": output_files_resource,
    },
    jobs=[etl_job],
    schedules=[etl_daily_schedule],
    sensors=[etl_sensor],
)

definitions = defs
