
from flask import Flask
app = Flask(__name__)

@app.route("/")
def health():
    return "✅ ARC_SUPERNOVA is alive and healthy", 200
