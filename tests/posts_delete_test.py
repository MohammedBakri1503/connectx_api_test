class TestPostsDelete:
    def test_delete_existing_post(self, posts_api):
        res = posts_api.delete(1)
        assert res.status_code in [200, 204]
