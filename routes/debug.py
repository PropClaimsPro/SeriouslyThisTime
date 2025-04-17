from flask import jsonify
def debug():
    return jsonify({"log": ["System active", "Agents deployed"]})