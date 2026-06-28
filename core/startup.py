from core.logger import logger
from core.profile import profile


def initialize():

    logger.info("Starting NOVA...")

    profile.refresh()

    logger.info("Profile Loaded")

    logger.info("Startup Complete")