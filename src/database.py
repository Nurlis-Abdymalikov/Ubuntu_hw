import sqlite3

class Database:
    def __init__(self, path: str):
        self.path = path
    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS todo(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    text NOT NULL,
                    category TEXT
                )
                """
            )