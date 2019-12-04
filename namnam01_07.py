import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()
query = """
    CREATE TABLE IF NOT EXISTS board (
        'idx' INTEGER PRIMARY KEY AUTOINCREMENT,
        'writer' VARCHAR(100),
        'title' VARCHAR(250),
        'contents' TEXT
    )
"""

cur.execute(query)


# query = "INSERT INTO board ('writer', 'title', 'contents') VALUES ('정하용', '제목', '내용입니다')"
query = "SELECT writer, title, contents FROM board"
cur.execute(query)

rows = cur.fetchall()
for rows in rows:
    print(rows)

conn.close()
# conn.commit()