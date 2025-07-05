from flask import Flask
import argparse

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello from Dev1ps!"

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=6060, help='Port to run on')
    args = parser.parse_args()
    app.run(host='0.0.0.0', port=args.port)