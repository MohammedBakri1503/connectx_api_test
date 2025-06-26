import pytest
from constants.http_status import OK, CREATED, NOT_FOUND, INTERNAL_SERVER_ERROR

class TestPostsUpdate:

    def test_update_post_title(self, posts_api, valid_post_data):
        """
        Positive test: update the title of a post.
        """
        updated_data = valid_post_data.copy()
        updated_data["title"] = "Updated Title"
        res = posts_api.update(1, updated_data)
        assert res.status_code == OK
        assert res.json()["title"] == "Updated Title"

    def test_update_post_body(self, posts_api, valid_post_data):
        """
        Positive test: update the body of a post.
        """
        updated_data = valid_post_data.copy()
        updated_data["body"] = "Updated Body"
        res = posts_api.update(1, updated_data)
        assert res.status_code == OK
        assert res.json()["body"] == "Updated Body"

    def test_update_post_with_invalid_data(self, posts_api, invalid_post_data):
        """
        Negative test: invalid types. JSONPlaceholder still accepts and returns 200.
        """
        res = posts_api.update(1, invalid_post_data)
        assert res.status_code == OK
        data = res.json()
        assert "title" in data or "userId" in data

    def test_update_non_existent_post(self, posts_api, valid_post_data):
        """
        Negative test: update a post with ID that doesn't exist.
        JSONPlaceholder returns 500.
        """
        res = posts_api.update(9999, valid_post_data)
        assert res.status_code == INTERNAL_SERVER_ERROR

    def test_update_post_with_empty_payload(self, posts_api, empty_post_data):
        """
        Edge case: empty dict. Still returns 200.
        """
        res = posts_api.update(1, empty_post_data)
        assert res.status_code == OK
        assert "id" in res.json()

    def test_update_post_with_none_payload(self, posts_api):
        """
        Invalid test: None as payload results in 200 (unexpected).
        """
        res = posts_api.update(1, None)
        assert res.status_code == OK
        assert "id" in res.json()

    def test_update_post_with_invalid_json(self, posts_api):
        """
        Bad JSON: string instead of dict. JSONPlaceholder throws 500.
        """
        res = posts_api.update(1, "Invalid JSON")
        assert res.status_code == INTERNAL_SERVER_ERROR

    def test_update_post_with_large_payload(self, posts_api, large_post_data):
        """
        Stress test: large body text.
        """
        res = posts_api.update(1, large_post_data)
        assert res.status_code == OK
        data = res.json()
        assert data["body"] == large_post_data["body"]

    def test_update_post_with_extra_fields(self, posts_api, extra_field_post_data):
        """
        Extra field: JSONPlaceholder includes unknown fields in response.
        """
        res = posts_api.update(1, extra_field_post_data)
        assert res.status_code == OK
        assert "extra_field" in res.json()

    def test_update_post_with_non_integer_id(self, posts_api, valid_post_data):
        """
        Non-integer ID ("abc") returns 500.
        """
        res = posts_api.update("abc", valid_post_data)
        assert res.status_code == INTERNAL_SERVER_ERROR

    def test_update_post_with_empty_id(self, posts_api, valid_post_data):
        """
        Empty string ID returns 404.
        """
        res = posts_api.update("", valid_post_data)
        assert res.status_code == NOT_FOUND

    def test_update_post_with_none_id(self, posts_api, valid_post_data):
        """
        None as ID returns 500.
        """
        res = posts_api.update(None, valid_post_data)
        assert res.status_code == INTERNAL_SERVER_ERROR
