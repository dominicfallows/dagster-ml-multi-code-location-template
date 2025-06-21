# This module extracts the vocabulary from the training data split.
from dagster import asset


@asset(name="create_vocab_from_training_data_asset",)
def create_vocab_from_training_data(context, split_tokenized_data_asset):
    """
    Extracts the vocabulary from the training data split.
    Args:
        context: Dagster context.
        split_tokenized_data_asset: Data splits with 'train' key.
    Returns:
        list[str]: List of vocabulary tokens.

    See Dagster concepts: https://docs.dagster.io/getting-started/concepts
    """
    train = split_tokenized_data_asset["train"]
    vocab = set()
    for row in train:
        vocab.update(row["tokens"])
    vocab_list = list(vocab)
    context.log.info(f"Extracted vocab: {vocab_list}")
    return vocab_list
