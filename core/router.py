class Router:

    def __init__(self):

        self.skills = []

    def register(self, skill):

        self.skills.append(skill)

    def process(self, command):

        for skill in self.skills:

            if skill.handle(command):
                return True

        return False


router = Router()