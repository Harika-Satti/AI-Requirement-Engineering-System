# Database Connection

import sqlite3


def get_connection():

    conn = sqlite3.connect(
        "requirements.db"
    )

    return conn


# create tables

def create_tables():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_name TEXT,
        requirement TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS documents(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER,
        document_type TEXT,
        content TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reviews(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER,
        review_report TEXT
    )
    """)

    conn.commit()
    conn.close()