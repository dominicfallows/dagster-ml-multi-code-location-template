import pytest
from 1_etl.1_ingest_data.assets import ingest_example_data


def test_ingest_example_data():
    data = ingest_example_data(None)
    assert isinstance(data, list)
    assert all("id" in row and "text" in row for row in data)
