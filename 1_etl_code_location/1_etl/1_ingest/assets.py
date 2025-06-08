from dagster import asset
from shared import shared_function

@asset(required_resource_keys={"raw_data_resource"})
def ingest_example_data(context):
    """
    Loads example data from the raw_data_resource Dagster resource.
    Returns:
        list[dict]: List of data rows with 'id' and 'text'.

    See Dagster concepts: https://docs.dagster.io/getting-started/concepts
    """
    try:
        example_data = context.resources.raw_data_resource
        context.log.info(f"Ingesting example data: {example_data}")
        return example_data
    except Exception as e:
        context.log.error(f"Failed to load example data: {e}")
        return []
