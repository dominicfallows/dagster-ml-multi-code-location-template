# Dagster definitions for the deploy code location
from dagster import Definitions, SourceAsset
from .assets import deploy_model_asset
from shared.resources import output_dir_resource

train_model_asset = SourceAsset("train_model_asset")

definitions = Definitions(
    assets=[deploy_model_asset, train_model_asset],
    resources={"output_dir_resource": output_dir_resource}
)
