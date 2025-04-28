import sqlite3

class ExpenseDB:
    def __init__(self, db_name="expenses.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    amount REAL NOT NULL
                )
            ''')

    def add_expense(self, name, amount):
        with self.conn:
            self.conn.execute(
                "INSERT INTO expenses (name, amount) VALUES (?, ?)",
                (name, amount)
            )

    def get_all_expenses(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name, amount FROM expenses")  # ← добавил id
        return cursor.fetchall()

    def get_total_amount(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT SUM(amount) FROM expenses")
        result = cursor.fetchone()[0]
        return result if result else 0.0

    def delete_expense(self, expense_id):
        with self.conn:
            self.conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))

