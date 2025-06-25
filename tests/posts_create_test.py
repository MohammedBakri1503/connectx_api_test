import pytest

class TestPostsCreate:
    def test_create_valid_post(self, posts_api, valid_post_data):
        res = posts_api.create(valid_post_data)
        assert res.status_code == 201
        data = res.json()
        assert data["title"] == valid_post_data["title"]

    def test_create_invalid_post(self, posts_api, invalid_post_data):
        res = posts_api.create(invalid_post_data)
        assert res.status_code == 201  # JSONPlaceholder allows this (not real API behavior)
