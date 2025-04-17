from flask import jsonify
def trigger_phase(phase):
    return jsonify({"phase_triggered": phase})