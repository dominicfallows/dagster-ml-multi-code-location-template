from dagster import resource
import json
import os


@resource
def input_files_resource(_):
    """Loads example data from a JSON file as a Dagster resource."""
    # Determine absolute path to raw_input_data.json
    base_dir = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "..", ".."))
    file_path = os.path.join(
        base_dir, "example_input_files_resource", "raw_input_data.json")
    with open(file_path) as f:
        return json.load(f)


@resource
def output_files_resource(_):
    """Returns the output directory for pipeline artifacts."""
    return "example_output_files_resource"
