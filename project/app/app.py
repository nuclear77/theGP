from flask import Flask, jsonify, request
import argparse
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Counter, Histogram
import time

app = Flask(__name__)

REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP Requests',
    ['method', 'endpoint', 'http_status']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP Request Latency',
    ['method', 'endpoint']
)


@app.route('/')
def home():
    return "test 123"


@app.route('/health')
def health():
    return jsonify({"status": "OK"})


@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}


@app.after_request
def after_request(response):
    REQUEST_COUNT.labels(
        request.method,
        request.path,
        response.status_code
    ).inc()

    if request.path != '/metrics':
        latency = time.time() - request.start_time
        REQUEST_LATENCY.labels(
            request.method,
            request.path
        ).observe(latency)

    return response


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=6060, help='Port to run on')
    args = parser.parse_args()


    @app.before_request
    def start_timer():
        request.start_time = time.time()


    app.run(host='0.0.0.0', port=args.port)
