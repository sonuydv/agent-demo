import sqlite3


def get_connection():
    conn = sqlite3.connect("chat_history.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT NOT NULL,
        first_name TEXT ,
        role TEXT NOT NULL,
        content TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.execute("""
                 CREATE INDEX IF NOT EXISTS idx_messages_user_id
                     ON messages(user_id)
                 """)

    conn.commit()
    conn.close()