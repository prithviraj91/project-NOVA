from memory.manager import memory


class UserProfile:

    def __init__(self):

        self.refresh()

    def refresh(self):

        self.name = memory.recall("name")
        self.favorite_game = memory.recall("favorite_game")
        self.favorite_food = memory.recall("favorite_food")

    def summary(self):

        lines = []

        if self.name:
            lines.append(f"Name: {self.name}")

        if self.favorite_game:
            lines.append(f"Favourite Game: {self.favorite_game}")

        if self.favorite_food:
            lines.append(f"Favourite Food: {self.favorite_food}")

        return "\n".join(lines)


profile = UserProfile()