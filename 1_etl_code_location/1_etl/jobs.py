from dagster import define_asset_job
from .config import ops

# Job to materialize all ETL assets
etl_job = define_asset_job(
    name="etl_job",
    selection=[
        "ingest_data_asset",
        "tokenized_data_asset",
        "split_tokenized_data_asset",
        "create_vocab_from_training_data_asset",
    ],
    config={"ops": ops},
)
