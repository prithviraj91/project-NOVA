import re

from memory.manager import memory


class MemoryEngine:

    def process(self, text):

        text = text.strip()

        # -------------------
        # Name
        # -------------------

        match = re.search(r"my name is (.+)", text, re.IGNORECASE)

        if match:

            memory.remember(
                "profile",
                "name",
                match.group(1)
            )

            return True

        # -------------------
        # Favourite Game
        # -------------------

        match = re.search(
            r"my favourite game is (.+)",
            text,
            re.IGNORECASE
        )

        if match:

            memory.remember(
                "preferences",
                "favorite_game",
                match.group(1)
            )

            return True

        # -------------------
        # Favourite Food
        # -------------------

        match = re.search(
            r"my favourite food is (.+)",
            text,
            re.IGNORECASE
        )

        if match:

            memory.remember(
                "preferences",
                "favorite_food",
                match.group(1)
            )

            return True

        return False


engine = MemoryEngine()