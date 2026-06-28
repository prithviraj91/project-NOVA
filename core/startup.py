from core.logger import logger
from core.skill_loader import load_skills
from core.dashboard import show_dashboard


def initialize():

    logger.info("===================================")
    logger.info("Starting NOVA ENGINE")

    load_skills()

    logger.info("Startup Complete")

    logger.info("===================================")

    show_dashboard()