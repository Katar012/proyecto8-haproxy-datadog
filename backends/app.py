from flask import Flask
import socket

app = Flask(__name__)
hostname = socket.gethostname()

@app.route("/")
def index():
    return f"Response from {hostname}\n"

@app.route("/metrics")
def metrics():
    return "requests_total 1\n"

app.run(host="0.0.0.0", port=80)