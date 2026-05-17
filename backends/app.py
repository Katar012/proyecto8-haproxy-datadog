from flask import Flask, request, render_template, jsonify
import os
import socket
import paramiko
import tempfile

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

node_id = os.getenv("NODE_ID", socket.gethostname())
SFTP_HOST = "192.168.65.20"
SFTP_PORT = 22

SFTP_USER = "sftpuser"
SFTP_PASS = "1234"

REMOTE_DIR = "/uploads"

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

    try:

        # Guardar temporal local
        temp = tempfile.NamedTemporaryFile(delete=False)

        file.save(temp.name)

        # Conexión SFTP
        transport = paramiko.Transport((SFTP_HOST, SFTP_PORT))

        transport.connect(
            username=SFTP_USER,
            password=SFTP_PASS
        )

        sftp = paramiko.SFTPClient.from_transport(transport)
        remote_path = f"{REMOTE_DIR}/{file.filename}"

        # Upload remoto
        sftp.put(temp.name, remote_path)

        # Cerrar conexión
        sftp.close()
        transport.close()

        # Eliminar temporal
        os.remove(temp.name)

        return jsonify({
            "status": "uploaded",
            "node": node_id,
            "remote_path": remote_path
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500

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
