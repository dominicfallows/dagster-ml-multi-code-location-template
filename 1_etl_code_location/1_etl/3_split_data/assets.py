# Dagster asset for split step
from dagster import asset, Config

class SplitConfig(Config):
    train_ratio: float = 0.6  # Default: 60% train
    validate_ratio: float = 0.2  # Default: 20% validate
    # Remaining is test

@asset(config_schema=SplitConfig)
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
    total = len(tokenize_asset)
    train_end = int(total * context.asset_config.train_ratio)
    validate_end = train_end + int(total * context.asset_config.validate_ratio)
    train = tokenize_asset[:train_end]
    validate = tokenize_asset[train_end:validate_end]
    test = tokenize_asset[validate_end:]
    context.log.info(f"Train split: {train}")
    context.log.info(f"Validate split: {validate}")
    context.log.info(f"Test split: {test}")
    return {"train": train, "validate": validate, "test": test}
