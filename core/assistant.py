from core.logger import logger
from core.pipeline import pipeline
from core.router import router
from core.history import history


from ai.chat import chat


class Assistant:

    def __init__(self):
        logger.info("Assistant initialized.")

    def process(self, command):
        history.add(command)

        # Pass through the pipeline
        command = pipeline.process(command)

        if command is None:
            return

        # Let a skill handle it
        if router.route(command):
            return

        # Otherwise use AI
        logger.ai("Sending prompt to AI...")

        reply = chat(command)

        print(f"\nNOVA: {reply}\n")


assistant = Assistant()