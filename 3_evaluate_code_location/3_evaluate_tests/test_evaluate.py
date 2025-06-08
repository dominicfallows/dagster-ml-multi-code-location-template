import pytest
from 3_evaluate.assets import evaluate_model_asset

class DummyContext:
    def __init__(self):
        self.log = type("log", (), {"info": print})()

def test_evaluate_model_asset():
    dummy_model = {"vocab_size": 4, "grouped_vocab": [["hello", "hi"], ["world"]]}
    dummy_split = {
        "test": [
            {"tokens": ["hello", "world", "foo"]},
            {"tokens": ["hi", "bar"]},
        ],
        "validate": [
            {"tokens": ["hello", "baz"]}
        ],
        "train": [
            {"tokens": ["hi", "world"]}
        ]
    }
    # Call the asset's compute_fn directly
    result = evaluate_model_asset.compute_fn(DummyContext(), dummy_model, dummy_split)
    assert isinstance(result, dict)
    assert abs(result["accuracy"] - 0.6) < 1e-6
