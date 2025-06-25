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
