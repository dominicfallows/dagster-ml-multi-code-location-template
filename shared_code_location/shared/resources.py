from dagster import resource
import json
import os


@resource
def raw_data_resource(_):
    """Loads example data from a JSON file as a Dagster resource."""
    # Determine absolute path to raw_data.json
    base_dir = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "..", ".."))
    file_path = os.path.join(base_dir, "example_resources", "raw_data.json")
    with open(file_path) as f:
        return json.load(f)


@resource
def output_dir_resource(_):
    """Returns the output directory for pipeline artifacts."""
    return "example_resources"
