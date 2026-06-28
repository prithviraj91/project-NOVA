import json
import os


def load_apps():
    with open("data/installed_apps.json", "r", encoding="utf-8") as file:
        return json.load(file)


OPEN_WORDS = (
    "open",
    "launch",
    "start",
    "run"
)


def handle(command):

    command = command.lower().strip()

    # Only continue if user intends to open something
    if not command.startswith(OPEN_WORDS):
        return False

    # Remove the opening verb
    for word in OPEN_WORDS:
        if command.startswith(word):
            app_name = command[len(word):].strip()
            break

    apps = load_apps()

    for name, path in apps.items():

        if name.lower() == app_name:

            try:
                os.startfile(path)
                print(f"Opened {name}")
                return True

            except Exception as e:
                print(e)
                return True

    return False