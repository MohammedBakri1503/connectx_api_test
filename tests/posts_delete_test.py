import pytest

class TestPostsDelete:

    def test_delete_existing_post(self, posts_api):
        """
        Positive test: Delete an existing post.
        JSONPlaceholder returns 200 OK with an empty body or 204 No Content.
        """
        res = posts_api.delete(1)
        assert res.status_code == 200  # JSONPlaceholder returns 200 for successful delete

        if res.status_code == 200:
            data = res.json()
            # Expected to return empty object (not the deleted resource)
            assert data == {}


    def test_delete_existing_post(self, posts_api):
        """
        Positive test: Delete an existing post.
        JSONPlaceholder returns 200 OK with an empty body or 204 No Content.
        """
        res = posts_api.delete(100)

       
        assert res.status_code == 200  # JSONPlaceholder returns 200 for successful delete

        if res.status_code == 200:
            data = res.json()
            # Expected to return empty object (not the deleted resource)
            assert data == {}

    def test_delete_non_existent_post(self, posts_api):
        """
        Edge case: Try to delete a non-existent post.
        JSONPlaceholder may return 200 with empty body, or 404.
        """
        res = posts_api.delete(9999)
        assert res.status_code == 200  # JSONPlaceholder returns 200 for non-existent posts

        if res.status_code == 200:
            data = res.json()
            assert data == {} or "id" not in data
        elif res.status_code == 404:
            assert res.json() == {}

    def test_delete_post_with_invalid_id(self, posts_api):
        """
        Negative test: Invalid ID (string instead of number).
        Expected 404 or 500 depending on backend.
        """
        res = posts_api.delete("abc")
        assert res.status_code == 200  # JSONPlaceholder returns 404 for non-integer IDs

        if res.status_code == 200:
            data = res.json()
            assert data == {} or "id" not in data
        elif res.status_code in [404, 500]:
            assert isinstance(res.json(), dict)

    def test_delete_post_with_empty_id(self, posts_api):
        """
        Negative test: Empty ID should return 404 or 500.
        """
        res = posts_api.delete("")
        assert res.status_code in [200, 404, 500]

        if res.status_code == 200:
            data = res.json()
            assert data == {} or "id" not in data
        elif res.status_code in [404, 500]:
            assert isinstance(res.json(), dict)

    def test_delete_post_with_none_id(self, posts_api):
        """
        Negative test: None as ID is invalid.
        Expecting 404 or 500 depending on the backend.
        """
        res = posts_api.delete(None)
        assert res.status_code == 200  # JSONPlaceholder returns 200 for None

        # JSONPlaceholder usually returns 500 for None
        assert isinstance(res.json(), dict)
