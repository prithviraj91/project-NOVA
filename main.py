from core.assistant import assistant
from core.startup import initialize


def main():

    initialize()

    print("\nNOVA OS is ready.\n")

    while True:

        command = input("You: ").strip()

        if not command:
            continue

        if command.lower() in ["exit", "quit"]:
            print("\nNOVA: Goodbye, Prithvi!\n")
            break

        assistant.process(command)


if __name__ == "__main__":
    main()