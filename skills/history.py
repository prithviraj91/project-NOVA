from core.history import history


class HistorySkill:

    def handle(self, command):

        command = command.lower()

        if command == "last command":

            last = history.last()

            if last:
                print(f"\nNOVA: Your last command was '{last}'.\n")
            else:
                print("\nNOVA: No previous command.\n")

            return True

        return False


history_skill = HistorySkill()