class TestPostsUpdate:
    def test_update_post_title(self, posts_api, valid_post_data):
        updated_data = valid_post_data.copy()
        updated_data["title"] = "Updated Title"
        res = posts_api.update(1, updated_data)
        assert res.status_code == 200
        assert res.json()["title"] == "Updated Title"
