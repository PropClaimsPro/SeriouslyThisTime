from flask import Blueprint, jsonify
import sqlite3

profit_routes = Blueprint('profit_routes', __name__)

@profit_routes.route("/profits", methods=["GET"])
def get_profits():
    conn = sqlite3.connect("vault_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, event FROM profits ORDER BY id DESC LIMIT 100")
    logs = cursor.fetchall()
    conn.close()
    return jsonify([{"timestamp": row[0], "event": row[1]} for row in logs])