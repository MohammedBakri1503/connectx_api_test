import json
import pytest

@pytest.fixture
def valid_payload():
    with open("data/post_payloads.json") as f:
        return json.load(f)["valid_post"]

@pytest.fixture
def invalid_payload():
    with open("data/post_payloads.json") as f:
        return json.load(f)["invalid_post"]
