import unittest
from app import app


class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_hello_route(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Hello, world!")


# ↓↓↓ ADD THIS LINE ↓↓↓
if __name__ == "__main__":
    unittest.main()
