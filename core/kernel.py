from core.router import router
from core.logger import logger
from core.profile import profile


class Kernel:

    def __init__(self):

        self.router = router
        self.logger = logger
        self.profile = profile


kernel = Kernel()