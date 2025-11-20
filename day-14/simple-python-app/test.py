import unittest
from app import app


class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_hello_route(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Version 2.0", response.data.decode())

    def test_health_route(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertIn("healthy", response.data.decode())

    def test_info_route(self):
        response = self.client.get("/info")
        self.assertEqual(response.status_code, 200)
        self.assertIn("CodePipeline test successful", response.data.decode())


if __name__ == "__main__":
    unittest.main()
