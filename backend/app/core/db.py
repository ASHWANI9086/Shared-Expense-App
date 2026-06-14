import sqlite3

DB_PATH = "expense.db"

class DB:
    @staticmethod
    def get_conn():
        conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        return conn

    @staticmethod
    def init():
        conn = DB.get_conn()
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            description TEXT,
            paid_by TEXT,
            amount REAL,
            currency TEXT,
            split_type TEXT,
            split_with TEXT,
            split_details TEXT,
            notes TEXT
        )
        """)

        conn.commit()
        conn.close()