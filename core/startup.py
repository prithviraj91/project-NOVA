from core.logger import logger
from core.router import router
from skills.browser import browser
from core.dashboard import show_dashboard
from skills.history import history_skill
from skills.apps import apps


def initialize():

    logger.info("===================================")
    logger.info("Starting NOVA OS...")

    router.register(apps)
    router.register(browser)
    router.register(history_skill)

    logger.info("Apps Skill Loaded")

    logger.info("Startup Complete")
    logger.info("===================================")
    show_dashboard()