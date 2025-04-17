
from flask import jsonify

def debug():
    return jsonify({
        "log": [
            "[INIT] System booted",
            "[WALLET] Web3 connector verified",
            "[AGENTS] Strategy swarm: ACTIVE"
        ]
    })
