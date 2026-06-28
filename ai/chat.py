import ollama

from memory.engine import engine
from memory.manager import memory
from core.context import context
CURRENT_PERSONALITY = "nova"

conversation = []


def load_personality():
    with open(
        f"config/personality/{CURRENT_PERSONALITY}.txt",
        "r",
        encoding="utf-8"
    ) as file:
        return file.read()


def set_personality(name):
    global CURRENT_PERSONALITY
    CURRENT_PERSONALITY = name

def chat(prompt):

    global conversation

    system_prompt = load_personality()

    # Automatically save important information
    engine.process(prompt)

    # Add relevant memories
    ctx = context.build(prompt)

    full_prompt = f""" 

    Known facts:

    {ctx["memory"]}

    User:
    
    {ctx["prompt"]}

    """


    # First message
    if len(conversation) == 0:

        conversation.append({
            "role": "system",
            "content": system_prompt
        })

    # User message
    conversation.append({
        "role": "user",
        "content": full_prompt
    })

    # Ask Ollama
    response = ollama.chat(
        model="llama3.2",
        messages=conversation
    )

    reply = response["message"]["content"]

    # Save assistant reply
    conversation.append({
        "role": "assistant",
        "content": reply
    })

    return reply