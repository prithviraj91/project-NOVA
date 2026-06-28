from memory.manager import memory


class ContextManager:

    def build(self, prompt):

        memories = memory.search(prompt)

        memory_context = ""

        for category, key, value in memories:
            memory_context += f"- {key}: {value}\n"

        return {

            "memory": memory_context,

            "prompt": prompt

        }


context = ContextManager()