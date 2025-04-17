
from flask import jsonify

def trigger_phase(phase):
    return jsonify({
        "event": "trigger_phase",
        "phase": phase,
        "result": f"✅ Phase {phase} escalation triggered."
    })
