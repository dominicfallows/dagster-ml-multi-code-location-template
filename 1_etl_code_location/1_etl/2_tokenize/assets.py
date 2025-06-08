# Dagster asset for tokenization step
from dagster import asset
from shared.tokenizer import simple_tokenizer

@asset
def tokenize_asset(context, ingest_example_data):
    """
    Tokenizes the ingested example data using a shared tokenizer.
    Args:
        context: Dagster context.
        ingest_example_data: List of ingested data rows.
    Returns:
        list[dict]: List of tokenized data rows.

    See Dagster concepts: https://docs.dagster.io/getting-started/concepts
    """
    # Use shared simple_tokenizer for consistency
    tokenized = [
        {"id": row["id"], "tokens": simple_tokenizer(row["text"])} for row in ingest_example_data
    ]
    context.log.info(f"Tokenized data: {tokenized}")
    return tokenized
