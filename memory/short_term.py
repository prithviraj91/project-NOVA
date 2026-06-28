conversation = []


def add(role, text):

    conversation.append({

        "role": role,

        "content": text

    })


def history():

    return conversation


def clear():

    conversation.clear()