import sqlite3

DB = "data/nova_memory.db"


def init_database():

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memories(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            category TEXT,

            key TEXT UNIQUE,

            value TEXT,

            created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_memory(category, key, value):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO memories
        (category,key,value)
        VALUES(?,?,?)
    """,(category,key,value))

    conn.commit()

    conn.close()


def get_memory(key):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT value FROM memories WHERE key=?",
        (key,)
    )

    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]

    return None


def get_all():

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT category,key,value FROM memories"
    )

    result = cursor.fetchall()

    conn.close()

    return result
def search_memories(text):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT category,key,value FROM memories"
    )

    memories = cursor.fetchall()

    conn.close()

    results = []

    text = text.lower()

    for category, key, value in memories:

        if key.lower() in text:
            results.append((category, key, value))

        elif value.lower() in text:
            results.append((category, key, value))

    return results 