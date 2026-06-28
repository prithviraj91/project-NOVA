import importlib
import os

from core.router import router
from core.logger import logger


def load_skills():

    skills_folder = "skills"

    for filename in os.listdir(skills_folder):

        if filename.startswith("_"):
            continue

        if not filename.endswith(".py"):
            continue

        module_name = filename[:-3]

        try:

            module = importlib.import_module(
                f"skills.{module_name}"
            )

            # Look for any object with a handle() method
            for obj in module.__dict__.values():

                if hasattr(obj, "handle"):

                    router.register(obj)

                    logger.info(
                        f"Loaded Skill: {module_name}"
                    )

        except Exception as e:

            logger.error(
                f"Failed loading {module_name}: {e}"
            )