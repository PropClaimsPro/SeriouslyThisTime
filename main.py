from flask import Flask, jsonify

# Initialize Flask app
app = Flask(__name__)

# ✅ Health check endpoint (used by DigitalOcean)
@app.route("/", methods=["GET"])
def health_check():
    return "✅ ARC_SUPERNOVA is alive and healthy", 200

# ✅ Optional: Status endpoint for app insight
@app.route("/status", methods=["GET"])
def status():
    return jsonify({
        "status": "active",
        "phase": "1-2-3",
        "strategies": 8,
        "version": "superstack-3.0"
    }), 200

# ✅ Optional: Phase controller endpoint
@app.route("/trigger/phase4", methods=["POST"])
def trigger_phase4():
    # You would call phase4.init() or similar from your actual logic
    return jsonify({
        "message": "Phase 4 trigger received. Boot sequence initiating..."
    }), 202

# 🧠 Reminder: We do NOT call app.run() here
# Gunicorn will take care of serving this application
