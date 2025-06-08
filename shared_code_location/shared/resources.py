from dagster import resource
import json

@resource
def raw_data_resource(_):
    """Loads example data from a JSON file as a Dagster resource."""
    with open("example_resources/raw_data.json") as f:
        return json.load(f)

@resource
def output_dir_resource(_):
    """Returns the output directory for pipeline artifacts."""
    return "example_resources"
