import sqlite3
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