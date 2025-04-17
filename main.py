from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# Health check endpoint for DigitalOcean
@app.route("/")
def health():
    return "✅ ARC_SUPERNOVA is alive and healthy", 200

# No need to call app.run(); gunicorn handles it
# If running locally, you can optionally include:
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8501)
