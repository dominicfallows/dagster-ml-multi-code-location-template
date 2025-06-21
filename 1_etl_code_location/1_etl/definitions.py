from dagster import Definitions, load_assets_from_modules
from shared.resources import input_files_resource, output_files_resource
import importlib
from .jobs import etl_job
from .schedules import etl_daily_schedule
from .sensors import etl_sensor

ingest = importlib.import_module(".1_ingest.assets", __package__)
tokenize = importlib.import_module(".2_tokenize.assets", __package__)
split = importlib.import_module(".3_split_data.assets", __package__)
vocab = importlib.import_module(".4_vocab_from_train_data.assets", __package__)

defs = Definitions(
    assets=load_assets_from_modules([
        ingest,
        tokenize,
        split,
        vocab
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
