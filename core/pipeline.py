from core.logger import logger


class Pipeline:

    def __init__(self):
        self.steps = []

    def add(self, step):
        self.steps.append(step)

    def process(self, command):

        logger.info(f"Pipeline started: {command}")

        for step in self.steps:

            command = step(command)

            if command is None:
                return None

        return command


pipeline = Pipeline()