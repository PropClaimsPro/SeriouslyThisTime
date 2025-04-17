from flask import jsonify
def status():
    return jsonify({"status": "LIVE", "phase": "1-2-3", "wallet": "✓", "signal": True})