from dagster import asset
import json


@asset(required_resource_keys={"output_files_resource"})
def deploy_model_asset(context, train_model_asset):
    """
    Saves the model as a mock ONNX file in the output_files_resource directory.
    Args:
        context: Dagster context.
        train_model_asset: The trained model to deploy.
    Returns:
        str: Path to the exported model file.

    See Dagster concepts: https://docs.dagster.io/getting-started/concepts
    """
    output_path = f"{context.resources.output_files_resource}/deployed_model.onnx.json"
    with open(output_path, "w") as f:
        json.dump(train_model_asset, f)
    context.log.info(f"Model exported to {output_path}")
    return output_path
