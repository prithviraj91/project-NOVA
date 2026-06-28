from matplotlib import text

from memory.database import *

from memory.short_term import *


class MemoryManager:

    def __init__(self):

        init_database()

    def remember(self, category, key, value):

        save_memory(category, key, value)

    def recall(self, key):

        return get_memory(key)
    def search(self, text):

        return search_memories(text)

    def remember_chat(self, role, text):

        add(role, text)

    def conversation(self):

        return history()


memory = MemoryManager()