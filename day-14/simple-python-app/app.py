from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, world! Version 2.0 - Pipeline Test!"


@app.route("/health")
def health():
    return {"status": "healthy", "version": "2.0"}


@app.route("/info")
def info():
    return {
        "message": "CodePipeline test successful!",
        "environment": os.getenv("ENVIRONMENT", "development"),
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
