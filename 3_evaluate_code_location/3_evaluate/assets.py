from dagster import asset, SourceAsset


train_model_asset = SourceAsset("train_model_asset")
split_asset = SourceAsset("split_asset")


@asset
def evaluate_model_asset(context, train_model_asset, split_asset):
    """
    Evaluates the model on the test set by checking how many tokens are in the model's grouped vocabulary.
    Args:
        context: Dagster context.
        train_model_asset (dict): Model output with 'grouped_vocab' key.
        split_asset (dict): Data splits with 'test' key.
    Returns:
        dict: {"accuracy": float}
    """
    test = split_asset.get("test", [])
    # Flatten grouped_vocab to a set
    grouped_vocab = train_model_asset.get("grouped_vocab", [])
    vocab = set()
    for group in grouped_vocab:
        vocab.update(group)
    total = 0
    in_vocab = 0
    for row in test:
        tokens = row.get("tokens", [])
        total += len(tokens)
        in_vocab += sum(1 for t in tokens if t in vocab)
    accuracy = in_vocab / total if total > 0 else 0.0
    context.log.info(
        f"Evaluation accuracy: {accuracy:.3f} ({in_vocab}/{total} tokens in vocab)")
    return {"accuracy": accuracy}
