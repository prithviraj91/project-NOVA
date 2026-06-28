import sqlite3


DB = "data/memory.db"


def remember(key, value):

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS memory (key TEXT PRIMARY KEY, value TEXT)"
    )

    cursor.execute(
        "INSERT OR REPLACE INTO memory VALUES (?, ?)",
        (key, value)
    )

    conn.commit()
    conn.close()


def recall(key):

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT value FROM memory WHERE key=?",
        (key,)
    )

    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]

    return None


def handle(command):

    command = command.lower().strip()

    # Remember favourite game
    if command.startswith("remember my favourite game is"):

        game = command.replace(
            "remember my favourite game is",
            "",
            1
        ).strip()

        remember("favorite_game", game)

        print(f"NOVA:\nI'll remember your favourite game is {game}.")

        return True

    # Recall favourite game
    if "what is my favourite game" in command:

        game = recall("favorite_game")

        if game:
            print(f"NOVA:\nYour favourite game is {game}.")
        else:
            print("NOVA:\nI don't know your favourite game yet.")

        return True

    return False