from flask import Flask, jsonify, send_file, request
import boto3
import os

app = Flask(__name__)

S3_BUCKET = os.environ["S3_BUCKET"]
s3 = boto3.client("s3")

@app.route("/api/meta")
def meta():
    return jsonify({"name": "Vinayak", "type": "resume"})

@app.route("/api/resume")
def resume():
    s3.download_file(S3_BUCKET, "Resume.pdf", "/tmp/resume.pdf")
    return send_file("/tmp/resume.pdf")

@app.route("/api/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    s3.upload_fileobj(file, S3_BUCKET, "Resume.pdf")
    return {"status": "uploaded"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
