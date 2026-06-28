import json
import ollama


SYSTEM_PROMPT = """
You decide whether the user's message should be saved as long-term memory.

Return ONLY valid JSON.

Format:

{
  "remember": true,
  "category": "...",
  "key": "...",
  "value": "..."
}

or

{
  "remember": false
}

Remember information like:
- name
- birthday
- favourite things
- goals
- projects
- college
- occupation
- preferences

Do NOT remember:
- casual conversation
- jokes
- temporary requests
- greetings

Return JSON only.
"""


def analyze_memory(text):

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    try:
        return json.loads(response["message"]["content"])

    except Exception:

        return {
            "remember": False
        }