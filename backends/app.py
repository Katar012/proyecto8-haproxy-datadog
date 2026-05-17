from flask import Flask
import socket
import time

app = Flask(__name__)
hostname = socket.gethostname()

@app.route("/")
def index():
    return f"Response from {hostname}\n"

@app.route("/metrics")
def metrics():
    return "requests_total 1\n"

@app.route("/error")
def error():
    return "Internal Error", 500

@app.route("/slow")
def slow():
    time.sleep(2)
    return "Slow response\n"

app.run(host="0.0.0.0", port=80)
