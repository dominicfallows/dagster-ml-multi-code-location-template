from dagster import Definitions, load_assets_from_modules, SourceAsset
from shared.resources import output_dir_resource

from . import assets
from .definitions import definitions as defs

train_model_asset = SourceAsset("train_model_asset")

defs = Definitions(
    assets=[*load_assets_from_modules([assets]), train_model_asset],
    resources={"output_dir_resource": output_dir_resource}
)
