import json
import pytest
from api.posts_api import PostsAPI

@pytest.fixture
def posts_api():
    return PostsAPI()

@pytest.fixture
def valid_post_data():
    with open("data/post_payloads.json") as f:
        return json.load(f)["valid_post"]

@pytest.fixture
def invalid_post_data():
    with open("data/post_payloads.json") as f:
        return json.load(f)["invalid_post"]

@pytest.fixture
def incomplete_post_data():
    with open("data/post_payloads.json") as f:
        return json.load(f)["incomplete_post"]

@pytest.fixture
def extra_field_post_data():
    with open("data/post_payloads.json") as f:
        return json.load(f)["extra_field_post"]

@pytest.fixture
def empty_post_data():
    with open("data/post_payloads.json") as f:
        return json.load(f)["empty_post"]

@pytest.fixture
def large_post_data():
    with open("data/post_payloads.json") as f:
        return json.load(f)["large_post"]
