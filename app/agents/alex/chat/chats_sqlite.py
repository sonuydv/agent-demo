from db.sqlite_db import get_connection

def save_message(user_id: str, role: str, content: str):

    conn = get_connection()

    conn.execute(
        """
        INSERT INTO messages (user_id, role, content)
        VALUES (?, ?, ?)
        """,
        (user_id, role, content)
    )

    conn.commit()
    conn.close()


def get_chat_history(user_id: str, limit: int = 150):

    conn = get_connection()

    rows = conn.execute(
        """
        SELECT role, content
        FROM messages
        WHERE user_id = ?
        ORDER BY id DESC
        LIMIT ?
        """,
        (user_id, limit)
    ).fetchall()

    conn.close()

    # reverse because we fetched newest first
    rows = rows[::-1]

    return [
        {"role": r["role"], "content": r["content"]}
        for r in rows
    ]