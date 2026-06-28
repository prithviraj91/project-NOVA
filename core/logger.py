from datetime import datetime

from core.constants import DEBUG


class Logger:

    def _time(self):
        return datetime.now().strftime("%H:%M:%S")

    def info(self, text):

        if DEBUG:
            print(f"[{self._time()}] INFO : {text}")

    def memory(self, text):

        if DEBUG:
            print(f"[{self._time()}] MEMORY : {text}")

    def skill(self, text):

        if DEBUG:
            print(f"[{self._time()}] SKILL : {text}")

    def ai(self, text):

        if DEBUG:
            print(f"[{self._time()}] AI : {text}")

    def error(self, text):

        print(f"[{self._time()}] ERROR : {text}")


logger = Logger()