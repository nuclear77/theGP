import unittest
import requests
import os
import time


class FlaskAppIntegrationTests(unittest.TestCase):
    BASE_URL = f"http://localhost:{os.getenv('APP_PORT', '6060')}"
    TIMEOUT = 5

    def test_health_endpoint(self):
        response = requests.get(f"{self.BASE_URL}/health", timeout=self.TIMEOUT)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "OK"})

    def test_metrics_endpoint(self):
        requests.get(f"{self.BASE_URL}/health", timeout=self.TIMEOUT)
        requests.get(f"{self.BASE_URL}/", timeout=self.TIMEOUT)

        response = requests.get(f"{self.BASE_URL}/metrics", timeout=self.TIMEOUT)
        self.assertEqual(response.status_code, 200)
        self.assertIn("http_requests_total", response.text)
        self.assertIn("http_request_duration_seconds", response.text)

    def test_invalid_endpoint(self):
        response = requests.get(f"{self.BASE_URL}/invalid-endpoint-123", timeout=self.TIMEOUT)
        self.assertEqual(response.status_code, 404)

    def test_response_time(self):
        start_time = time.time()
        response = requests.get(f"{self.BASE_URL}/health", timeout=self.TIMEOUT)
        latency = time.time() - start_time

        self.assertLess(latency, 1, "Response time too slow")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()