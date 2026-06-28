from rich.console import Console
from rich.panel import Panel
from datetime import datetime
from voice.piper_voice import speak
from voice.listen import listen
from ai.brain import process_command
from memory.memory import create_database, save_memory,get_memory
import json

console = Console()

with open("config/settings.json", "r") as file:
    settings = json.load(file)


create_database()

assistant = settings["assistant_name"]
user = settings["user_name"]
current_hour=datetime.now().hour

if current_hour<12:
    greeting=" good morning"
elif current_hour<18:
    greeting=" good afternoon"
else:
    greeting="" \
    " good evening"
speak(f"{greeting}, {user}. I am {assistant}. How can I help you today?")


console.print(
    Panel.fit(
        f"""
🤖 Assistant : {assistant}

{greeting}, {user}!

Status : ONLINE

Awaiting your command...
""",
        title="PROJECT NOVA",
    )
)
WAKE_WORDS = [
    "nova",
    "hey nova",
    "ok nova"
]

while True:

    command = listen()

    if command == "":
        continue

    command = command.lower()

    # Wait for wake word
    if any(word in command for word in WAKE_WORDS):

        speak("Yes?")

        # Listen again for the actual command
        command = listen()

        if command:
            try:
                process_command(command)
            except Exception as e:
                print("\n=====================")
                print("ERROR INSIDE process_command:")
                print(e)
                print("=====================\n")
    

