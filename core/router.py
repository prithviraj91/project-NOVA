class Router:

    def __init__(self):
        self.skills = []

    def register(self, skill):
        self.skills.append(skill)

    def route(self, command):

        print("Router received:", command)
        print("Registered skills:", len(self.skills))

        for skill in self.skills:

            print("Trying:", skill)

            try:
                if skill.handle(command):
                    print("Handled!")
                    return True

            except Exception as e:
                print(f"Router Error: {e}")

        print("No skill handled the command.")
        return False


router = Router()