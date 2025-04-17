
from flask import jsonify

def status():
    return jsonify({
        "phase": "1-2-3",
        "status": "LIVE",
        "agents_active": 8,
        "wallet_status": "✓ CONNECTED",
        "signal_webhook": True
    })
