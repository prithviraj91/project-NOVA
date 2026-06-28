from ai.chat import chat, set_personality


class NovaEngine:

    def __init__(self):
        self.mode = "nova"

    def ask(self, prompt):
        return chat(prompt)

    def personality(self, mode):
        self.mode = mode
        set_personality(mode)


nova = NovaEngine()