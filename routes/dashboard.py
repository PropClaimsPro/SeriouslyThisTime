from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/logs")
def show_logs():
    conn = sqlite3.connect("vault_tracker.db")
    logs = conn.execute("SELECT timestamp, event FROM profits ORDER BY timestamp DESC LIMIT 50").fetchall()
    conn.close()
    return jsonify([{"timestamp": row[0], "event": row[1]} for row in logs])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)