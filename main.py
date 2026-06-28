from ai.brain import process_command

while True:

    command = input("You: ")

    if command.lower() == "exit":
        break

    process_command(command)