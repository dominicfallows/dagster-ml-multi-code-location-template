from dagster import asset


@asset(required_resource_keys={"input_files_resource"})
def ingest_example_data(context):
    """
    Loads example data from the input_files_resource Dagster resource.
    Returns:
        list[dict]: List of data rows with 'id' and 'text'.

    See Dagster concepts: https://docs.dagster.io/getting-started/concepts
    """
    try:
        example_data = context.resources.input_files_resource
        context.log.info(f"Ingesting example data: {example_data}")
        return example_data
    except Exception as e:
        context.log.error(f"Failed to load example data: {e}")
        return []
