import sqlite3

conn = sqlite3.connect(
    "requirements.db"
)

cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM projects"
)

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()