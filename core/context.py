from memory.manager import memory

from ai.chat import load_personality


class ContextManager:

    def build(self, prompt):

        system = load_personality()

        memories = memory.search(prompt)

        memory_context = ""

        for category, key, value in memories:

            memory_context += f"- {key}: {value}\n"

        return {

            "system": system,

            "memory": memory_context,

            "prompt": prompt

        }


context = ContextManager()