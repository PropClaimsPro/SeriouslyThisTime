from flask import jsonify
def report():
    return jsonify({"top_strategy": "HFT Blitz", "roi": "$300/min"})