import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify(status="ok", version=os.environ.get("VERSION", "dev"))


@app.get("/hello/<name>")
def hello(name: str):
    return jsonify(message=f"Hello, {name}!")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
