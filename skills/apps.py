import json
import os
from difflib import SequenceMatcher

from core.logger import logger
from core.events import events
from core.state import state


OPEN_WORDS = (
    "open",
    "launch",
    "start",
    "run"
)


def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()


class AppsSkill:

    def __init__(self):
        self.apps = self.load_apps()

    def load_apps(self):
        with open(
            "data/installed_apps.json",
            "r",
            encoding="utf-8"
        ) as file:
            return json.load(file)

    def handle(self, command):

        command = command.lower().strip()

        if not command.startswith(OPEN_WORDS):
            return False

        # Remove "open", "launch", etc.
        app_name = command

        for word in OPEN_WORDS:
            if command.startswith(word):
                app_name = command[len(word):].strip()
                break

        best_score = 0
        best_app = None

        for name, path in self.apps.items():

            app = name.lower()

            score = similarity(app_name, app)

            # Give bonus if the app name contains the user's words
            if app_name in app:
                score += 0.5

            if score > best_score:
                best_score = score
                best_app = (name, path)

        if best_app is None:
            return False

        # Don't open random apps if the match is poor
        if best_score < 0.45:
            return False

        name, path = best_app

        try:

            os.startfile(path)
            state.current_app = name
            state.last_command = command

            logger.skill(f"Opened {name}")

            events.emit(
                "app.opened",
                {
                    "name": name
                }
            )

            return True

        except Exception as e:

            logger.error(str(e))
            return True


apps = AppsSkill()