import pytest
from constants.http_status import OK, CREATED, NOT_FOUND, INTERNAL_SERVER_ERROR

class TestPostsGet:
    def test_get_all_posts(self, posts_api):
        res = posts_api.get_all()
        assert res.status_code == OK
        assert isinstance(res.json(), list)
        assert len(res.json()) == 100, "Expected non-empty list of posts"

    def test_all_posts_contains_expected_subset(self, posts_api):
        """
        Positive data integrity test:
        Ensures that a known subset of records exists in the full list returned from GET /posts.
        """
        expected_subset = [
            {
                "userId": 1,
                "id": 1,
                "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
                "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
            },
            {
                "userId": 1,
                "id": 2,
                "title": "qui est esse",
                "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
            },
            {
                "userId": 1,
                "id": 3,
                "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
                "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
            }
        ]

        res = posts_api.get_all()
        assert res.status_code == OK
        data = res.json()
        assert isinstance(data, list)
        for expected_post in expected_subset:
            assert expected_post in data, f"Expected post not found: {expected_post}"

    def test_get_post_valid_id_1(self, posts_api):
        res = posts_api.get_by_id(1)
        assert res.status_code == OK
        assert res.json()["id"] == 1

    def test_get_post_valid_id_100(self, posts_api):
        res = posts_api.get_by_id(100)
        assert res.status_code == OK
        assert res.json()["id"] == 100

    def test_get_post_valid_id_101(self, posts_api):
        res = posts_api.get_by_id(101)
        assert res.status_code == NOT_FOUND  # JSONPlaceholder returns 404 (Not found) for IDs > 100
        assert res.json() == {}

    def test_get_post_invalid_id(self, posts_api):
        res = posts_api.get_by_id(9999)
        assert res.status_code == NOT_FOUND  # JSONPlaceholder returns 404 for non-existent post
        assert res.json() == {}

    def test_get_post_non_integer_id(self, posts_api):
        res = posts_api.get_by_id("abc")
        assert res.status_code == NOT_FOUND  # JSONPlaceholder returns 404 for non-integer IDs
        assert res.json() == {} or "id" not in res.json()

    def test_get_post_empty_id(self, posts_api):
        res = posts_api.get_by_id("")
        assert res.status_code == OK
        data = res.json()
        assert isinstance(data, list)  # JSONPlaceholder returns an empty list for empty ID
        assert len(data) > 0

    def test_get_post_none_id(self, posts_api):
        res = posts_api.get_by_id(None)
        assert res.status_code == NOT_FOUND  # JSONPlaceholder returns 404 for None ID
        assert res.json() == {} or "id" not in res.json()
