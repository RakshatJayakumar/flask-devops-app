from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(
        {"message": "Flask DevOps App", "status": "healthy", "version": "1.0.0"}
    )


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/info")
def info():
    return jsonify(
        {
            "app": "Flask DevOps Pipeline",
            "author": "Rakshat Jayakumar",
            "stack": ["Flask", "Docker", "GitHub Actions", "AWS ECR", "EC2"],
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
