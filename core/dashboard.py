from core.state import state
from core.router import router
from core.constants import VERSION, MODEL


def show_dashboard():

    print("""
╔══════════════════════════════════════╗
║              NOVA ENGINE             ║
╚══════════════════════════════════════╝
""")

    print(f"Version        : {VERSION}")
    print(f"Model          : {MODEL}")

    print("\nSystem")
    print("----------------------------")
    print(f"Skills         : {len(router.skills)}")

    print("\nSession")
    print("----------------------------")
    print(f"App            : {state.current_app}")
    print(f"Website        : {state.current_website}")
    print(f"Google         : {state.last_google_search}")
    print(f"YouTube        : {state.last_youtube_search}")

    print("\nReady.\n")