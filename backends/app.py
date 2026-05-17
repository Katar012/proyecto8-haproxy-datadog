from flask import Flask, request, render_template, jsonify
import os
import socket

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

node_id = os.getenv("NODE_ID", socket.gethostname())

@app.route("/")
def index():
    return render_template("index.html", node=node_id)

@app.route("/upload", methods=["POST"])
def upload():

    if "file" not in request.files:
        return jsonify({"error": "no file"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "empty filename"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    return jsonify({
        "status": "uploaded",
        "node": node_id,
        "filename": file.filename
    })

@app.route("/files")
def files():

    files = os.listdir(UPLOAD_FOLDER)

    return jsonify({
        "node": node_id,
        "files": files
    })

@app.route("/metrics")
def metrics():
    return "requests_total 1\n"

@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "node": node_id
    })

app.run(host="0.0.0.0", port=80)
