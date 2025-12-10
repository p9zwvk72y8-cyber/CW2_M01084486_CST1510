


def create_user_table(conn):
    curr = conn.cursor()
    sql = (""" CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL
        ) """)
    curr.execute(sql)
    conn.commit()
