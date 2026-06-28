from core.logger import logger
from core.router import router

from skills.apps import apps


def initialize():

    logger.info("===================================")
    logger.info("Starting NOVA OS...")

    router.register(apps)

    logger.info("Apps Skill Loaded")

    logger.info("Startup Complete")
    logger.info("===================================")