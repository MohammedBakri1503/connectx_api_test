from api.base_api import BaseAPI

class PostsAPI(BaseAPI):
    def get_all(self):
        return self.get("/posts")

    def get_by_id(self, post_id):
        return self.get(f"/posts/{post_id}")

    def create(self, payload):
        return self.post("/posts", payload)

    def update(self, post_id, payload):
        return self.put(f"/posts/{post_id}", payload)

    def delete(self, post_id):
        return self.delete(f"/posts/{post_id}")
