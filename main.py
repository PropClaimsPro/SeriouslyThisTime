
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 ARC_SUPERNOVA is Live. Health check passed."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
