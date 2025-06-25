import pytest

class TestPostsGet:
    def test_get_all_posts(self, posts_api):
        res = posts_api.get_all()
        assert res.status_code == 200
        assert isinstance(res.json(), list)

    def test_get_post_valid_id(self, posts_api):
        res = posts_api.get_by_id(1)
        assert res.status_code == 200
        assert res.json()["id"] == 1

    def test_get_post_invalid_id(self, posts_api):
        res = posts_api.get_by_id(9999)
        assert res.status_code in [200, 404]
        assert res.json() == {} or "id" not in res.json()
