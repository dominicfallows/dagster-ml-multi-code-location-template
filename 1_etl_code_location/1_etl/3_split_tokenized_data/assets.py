# Dagster asset for split step
from dagster import asset, Field
from ..config import ops

# Retrieve the 'config' dict for this asset from ops
default_values = ops.get("split_tokenized_data_asset", {}).get("config", {})


@asset(
    name="split_tokenized_data_asset",
    config_schema={
        "train_ratio": Field(
            float,
            default_value=default_values.get("train_ratio"),
            description="Fraction for training split"
        ),
        "validate_ratio": Field(
            float,
            default_value=default_values.get("validate_ratio"),
            description="Fraction for validation split"
        ),
        "test_ratio": Field(
            float,
            default_value=default_values.get("test_ratio"),
            description="Fraction for test split"
        ),
    },
)
def split_example_tokenized_data(context, tokenized_data_asset):
    """
    Splits tokenized data into train, validate, and test sets using configurable ratios.
    Args:
        context: Dagster context (with config).
        tokenized_data_asset: List of tokenized data.
    Returns:
        dict: {"train": [...], "validate": [...], "test": [...]}

    See Dagster concepts: https://docs.dagster.io/getting-started/concepts
    """
    train_ratio = context.op_config.get("train_ratio")
    validate_ratio = context.op_config.get("validate_ratio")
    test_ratio = context.op_config.get("test_ratio")
    total_ratio = train_ratio + validate_ratio + test_ratio

    if not abs(total_ratio - 1.0) < 1e-6:
        raise ValueError(
            f"Ratios must sum to 1.0, but got {total_ratio} (train: {train_ratio}, validate: {validate_ratio}, test: {test_ratio})")

    total = len(tokenized_data_asset)
    train_end = int(total * train_ratio)
    validate_end = train_end + int(total * validate_ratio)

    train = tokenized_data_asset[:train_end]
    validate = tokenized_data_asset[train_end:validate_end]
    test = tokenized_data_asset[validate_end:]

    context.log.info(f"Train split: {train}")
    context.log.info(f"Validate split: {validate}")
    context.log.info(f"Test split: {test}")

    return {"train": train, "validate": validate, "test": test}
