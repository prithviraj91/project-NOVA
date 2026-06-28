class CommandHistory:

    def __init__(self):
        self.commands = []

    def add(self, command):
        self.commands.append(command)

    def last(self):
        if self.commands:
            return self.commands[-1]
        return None


history = CommandHistory()