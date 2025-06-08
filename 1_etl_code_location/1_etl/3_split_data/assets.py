# Dagster asset for split step
from dagster import asset


@asset(config_schema={
    "train_ratio": float,
    "validate_ratio": float,
})
def split_asset(context, tokenize_asset):
    """
    Splits tokenized data into train, validate, and test sets using configurable ratios.
    Args:
        context: Dagster context (with config).
        tokenize_asset: List of tokenized data.
    Returns:
        dict: {"train": [...], "validate": [...], "test": [...]}

    See Dagster concepts: https://docs.dagster.io/getting-started/concepts
    """
    train_ratio = context.asset_config.get("train_ratio", 0.6)
    validate_ratio = context.asset_config.get("validate_ratio", 0.2)
    total = len(tokenize_asset)
    train_end = int(total * train_ratio)
    validate_end = train_end + int(total * validate_ratio)
    train = tokenize_asset[:train_end]
    validate = tokenize_asset[train_end:validate_end]
    test = tokenize_asset[validate_end:]
    context.log.info(f"Train split: {train}")
    context.log.info(f"Validate split: {validate}")
    context.log.info(f"Test split: {test}")
    return {"train": train, "validate": validate, "test": test}
