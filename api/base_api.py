import requests

class BaseAPI:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get(self, endpoint):
        return requests.get(f"{self.BASE_URL}{endpoint}")

    def post(self, endpoint, payload):
        return requests.post(f"{self.BASE_URL}{endpoint}", json=payload)

    def put(self, endpoint, payload):
        return requests.put(f"{self.BASE_URL}{endpoint}", json=payload)

    def delete(self, endpoint):
        return requests.delete(f"{self.BASE_URL}{endpoint}")
