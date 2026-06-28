import webbrowser

from core.logger import logger
from core.events import events
from core.state import state


WEBSITES = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "github": "https://github.com",
    "gmail": "https://mail.google.com",
    "chatgpt": "https://chatgpt.com",
    "reddit": "https://www.reddit.com",
    "instagram": "https://www.instagram.com",
    "facebook": "https://www.facebook.com",
    "linkedin": "https://www.linkedin.com",
    "twitter": "https://x.com",
}


class BrowserSkill:

    def handle(self, command):

        command = command.lower().strip()

        # -----------------------
        # Open Website
        # -----------------------

        OPEN_WORDS = (
            "open",
            "launch",
            "go to"
        )

        for word in OPEN_WORDS:

            if command.startswith(word):

                website = command.replace(word, "", 1).strip()

                if website in WEBSITES:

                    webbrowser.open(WEBSITES[website])
                    state.current_website = website
                    state.last_command = command

                    logger.skill(f"Opened {website}")

                    events.emit(
                        "browser.opened",
                        {
                            "website": website
                        }
                    )

                    return True

        # -----------------------
        # Google Search
        # -----------------------

        if command.startswith("search google for"):

            query = command.replace(
                "search google for",
                "",
                1
            ).strip()

            webbrowser.open(
                "https://www.google.com/search?q="
                + query.replace(" ", "+")
            )
            state.last_google_search = query
            state.last_command = command


            logger.skill(f"Google search: {query}")

            events.emit(
                "google.search",
                {
                    "query": query
                }
            )

            return True

        # -----------------------
        # YouTube Search
        # -----------------------

        if command.startswith("search youtube for"):

            query = command.replace(
                "search youtube for",
                "",
                1
            ).strip()

            webbrowser.open(
                "https://www.youtube.com/results?search_query="
                + query.replace(" ", "+")
            )
            state.last_youtube_search = query
            state.last_command = command   

            logger.skill(f"YouTube search: {query}")

            events.emit(
                "youtube.search",
                {
                    "query": query
                }
            )

            return True

        return False


browser = BrowserSkill()