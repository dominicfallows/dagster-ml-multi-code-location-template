from dagster import define_asset_job
from . import assets
import importlib

ingest = importlib.import_module(".1_ingest.assets", __package__)
tokenize = importlib.import_module(".2_tokenize.assets", __package__)
split = importlib.import_module(".3_split_data.assets", __package__)
vocab = importlib.import_module(".4_vocab_from_train_data.assets", __package__)

# Job to materialize all ETL assets
etl_job = define_asset_job(
    name="etl_job",
    selection=[
        "ingest_example_data",
        "tokenize_asset",
        "split_asset",
        "vocab_from_train_data",
    ],
)
