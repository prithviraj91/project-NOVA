class Router:

    def __init__(self):
        self.skills = []

    def register(self, skill):
        self.skills.append(skill)

    def route(self, command):

        for skill in self.skills:

            try:

                if skill.handle(command):
                    return True

            except Exception as e:
                print(f"Router Error: {e}")

        return False


router = Router()