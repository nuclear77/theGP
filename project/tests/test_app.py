import unittest
import requests
import os


class FlaskAppIntegrationTests(unittest.TestCase):
    BASE_URL = f"http://localhost:{os.getenv('APP_PORT', '6060')}"
    TIMEOUT = 5

    def test_health_endpoint(self):
        response = requests.get(f"{self.BASE_URL}/health", timeout=self.TIMEOUT)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "OK"})

    def test_metrics_endpoint(self):
        response = requests.get(f"{self.BASE_URL}/metrics", timeout=self.TIMEOUT)
        self.assertEqual(response.status_code, 200)
        self.assertIn("http_requests_total", response.text)
        self.assertIn("python_gc_objects_collected_total", response.text)

    def test_invalid_endpoint(self):
        response = requests.get(f"{self.BASE_URL}/invalid-endpoint-123", timeout=self.TIMEOUT)
        self.assertEqual(response.status_code, 404)
        self.assertIn("Not Found", response.text)

    def test_response_time(self):
        response = requests.get(f"{self.BASE_URL}/health", timeout=self.TIMEOUT)
        self.assertLess(response.elapsed.total_seconds(), 1, "Response time too slow")


if __name__ == "__main__":
    unittest.main()