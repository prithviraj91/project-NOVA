from ai.chat import chat

from skills import apps,browser,memory


SKILLS = [
    apps,
    browser,
    memory
]


def process_command(command):

    command = command.lower().strip()

    for skill in SKILLS:

        if skill.handle(command):
            return

    response = chat(command)

    print("\nNOVA:\n")

    print(response)