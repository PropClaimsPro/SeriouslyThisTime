import sqlite3
import os
from datetime import datetime

class ProfitLogger:
    def __init__(self, db_path="vault_tracker.db"):
        self.db_path = db_path

    def initialize_db(self):
        conn = sqlite3.connect(self.db_path)
        conn.execute('''CREATE TABLE IF NOT EXISTS profits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            event TEXT
        )''')
        conn.commit()
        conn.close()

    def log_event(self, event):
        conn = sqlite3.connect(self.db_path)
        conn.execute("INSERT INTO profits (timestamp, event) VALUES (?, ?)", (datetime.utcnow().isoformat(), event))
        conn.commit()
        conn.close()

    def read_logs(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.execute("SELECT timestamp, event FROM profits ORDER BY id DESC LIMIT 100")
        logs = [{"timestamp": row[0], "event": row[1]} for row in cursor.fetchall()]
        conn.close()
        return logs