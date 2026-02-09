import sqlite3


def get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect("short_url.db")
    connection.row_factory = sqlite3.Row
    return connection


def init_db() -> None:
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Shorten(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                code TEXT UNIQUE NOT NULL,
                original_url TEXT NOT NULL
            )
            """
        )
        conn.commit()
