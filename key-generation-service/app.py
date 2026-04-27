import uuid

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/generate-key", methods=["GET"])
def generate_key():
    id = str(uuid.uuid4())
    return jsonify({"key": id}), 200
