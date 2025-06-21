from dagster import asset
import os
import json


@asset(name="output_materialized_assets", required_resource_keys={"output_files_resource"})
def output_materialized_assets(context, tokenized_data_asset, split_tokenized_data_asset, create_vocab_from_training_data_asset):
    """
    Writes materialized assets from prior steps to the output_files_resource folder.
    """
    base_output = context.resources.output_files_resource
    # Create subdirectories for each asset type
    tokenized_dir = os.path.join(base_output, "tokenized_data")
    split_dir = os.path.join(base_output, "split_tokenized_data")
    vocab_dir = os.path.join(base_output, "vocab")
    for d in [tokenized_dir, split_dir, vocab_dir]:
        os.makedirs(d, exist_ok=True)

    tokenized_path = os.path.join(tokenized_dir, "tokenized_data.json")
    with open(tokenized_path, "w") as f:
        json.dump(tokenized_data_asset, f)

    split_path = os.path.join(split_dir, "split_tokenized_data.json")
    with open(split_path, "w") as f:
        json.dump(split_tokenized_data_asset, f)

    vocab_path = os.path.join(vocab_dir, "vocab.json")
    with open(vocab_path, "w") as f:
        json.dump(create_vocab_from_training_data_asset, f)

    context.log.info(f"Wrote tokenized data to {tokenized_path}")
    context.log.info(f"Wrote split data to {split_path}")
    context.log.info(f"Wrote vocab to {vocab_path}")

    return {
        "tokenized_data_path": tokenized_path,
        "split_tokenized_data_path": split_path,
        "vocab_path": vocab_path,
    }
