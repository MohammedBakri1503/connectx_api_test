import pytest

class TestPostsCreate:
    def test_create_valid_post(self, posts_api, valid_post_data):
        """Positive test: creating a post with valid data should return 201 and the same title."""
        res = posts_api.create(valid_post_data)
        assert res.status_code == 201
        data = res.json()
        assert data["title"] == valid_post_data["title"]

    def test_create_invalid_post(self, posts_api, invalid_post_data):
        """
        Edge case: JSONPlaceholder still returns 201 even with invalid data.
        In a real API, this would be 400 Bad Request.
        """
        res = posts_api.create(invalid_post_data)
        assert res.status_code == 201
        data = res.json()
        assert "title" in data  # Because our invalid data still included "title"

    def test_create_post_without_required_fields(self, posts_api, incomplete_post_data):
        """
        Missing required fields like 'body' or 'userId'.
        JSONPlaceholder still returns 201 with only the fields you provide.
        """
        res = posts_api.create(incomplete_post_data)
        assert res.status_code == 201
        data = res.json()
        assert data["title"] == incomplete_post_data["title"]
        assert "id" in data

    def test_create_post_with_extra_fields(self, posts_api, extra_field_post_data):
        """
        Send extra/unexpected fields in payload.
        JSONPlaceholder will echo them back (not realistic for production APIs).
        """
        res = posts_api.create(extra_field_post_data)
        assert res.status_code == 201
        data = res.json()
        assert data["title"] == extra_field_post_data["title"]
        assert "extra_field" in data

    def test_create_post_with_empty_payload(self, posts_api, empty_post_data):
        """
        Edge case: Sending an empty dict still returns 201 and generates only an ID.
        """
        res = posts_api.create(empty_post_data)
        assert res.status_code == 201
        data = res.json()
        assert "id" in data
        assert "title" not in data

    def test_create_post_with_none_payload(self, posts_api):
        """
        Technically invalid: `None` is not valid JSON.
        JSONPlaceholder accepts it and still returns 201 with ID (for demo/testing).
        """
        res = posts_api.create(None)
        assert res.status_code == 201
        data = res.json()
        assert "id" in data

    def test_create_post_with_large_payload(self, posts_api, large_post_data):
        """
        Stress test: Send a very large body string.
        JSONPlaceholder accepts large payloads and returns them as-is.
        """
        res = posts_api.create(large_post_data)
        assert res.status_code == 201
        data = res.json()
        assert data["title"] == large_post_data["title"]
        assert data["body"] == large_post_data["body"]
        assert len(data["body"]) == len(large_post_data["body"])
