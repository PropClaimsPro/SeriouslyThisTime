
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Profit Engine Phase III is live and production-ready!"

@app.route("/healthz")
def health():
    return "OK", 200

# This allows Gunicorn to find 'app'
if __name__ != "__main__":
    application = app
