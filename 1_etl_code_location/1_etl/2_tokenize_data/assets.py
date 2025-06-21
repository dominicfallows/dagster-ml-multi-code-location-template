# Dagster asset for tokenization step
from dagster import asset
from shared.tokenizer import simple_tokenizer


@asset(name="tokenized_data_asset")
def tokenize_example_data(context, ingest_data_asset):
    """
    Tokenizes the ingested example data using a shared tokenizer.
    Args:
        context: Dagster context.
        ingest_data_asset: List of ingested data rows.
    Returns:
        list[dict]: List of tokenized data rows.

    See Dagster concepts: https://docs.dagster.io/getting-started/concepts
    """
    # Use shared simple_tokenizer for consistency
    tokenized = [
        {"id": row["id"], "tokens": simple_tokenizer(row["text"])} for row in ingest_data_asset
    ]
    context.log.info(f"Tokenized data: {tokenized}")
    return tokenized
