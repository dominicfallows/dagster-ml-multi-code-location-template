import json
import os

def save_to_disk(data, filename):
    """Save data as JSON to disk.
    Args:
        data: The data to save (serializable).
        filename (str): The file path to write to.
    Returns:
        str: The filename written.
    """
    with open(filename, "w") as f:
        json.dump(data, f)
    return filename

def load_from_disk(filename):
    """Load data from JSON file on disk.
    Args:
        filename (str): The file path to read from.
    Returns:
        The data loaded from the file.
    """
    with open(filename, "r") as f:
        return json.load(f)
