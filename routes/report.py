
from flask import jsonify

def report():
    return jsonify({
        "roi_last_5min": "$324.17",
        "top_strategy": "HFT AI Blitz",
        "agent_yield": {
            "HFT AI Blitz": "$127.40/min",
            "Cross-Exchange Arbitrage": "$98.23/min",
            "FlashLoan Strike": "$74.54/min"
        }
    })
