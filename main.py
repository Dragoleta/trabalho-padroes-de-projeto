import subprocess

from managerMenu import ManagerMenu
from menuLog import MenuLog
from userLogState import LoggedOutState, LogManager


class Main:
    def __init__(self, loginManager):
        self.jsonFile = "users.json"
        self.loginManager = loginManager

    def mainMenu(self):
        subprocess.run(["clear"])
        print("Welcome to the incredibly safe password manager")
        if isinstance(self.loginManager.get_state(), LoggedOutState):
            MenuLog.menu(loginManager=self.loginManager, filename=self.jsonFile)
            main.mainMenu()

        print("What do you wish to do?")
        action = str(
            input(
                """
1 - Manage your passwords
2 - Log Out
->"""
            )
        )

        match action:
            case "1":
                ManagerMenu.options(
                    user=self.loginManager.get_user(), filename=self.jsonFile
                )
                main.mainMenu()
            case "2":
                self.loginManager.logout()
                main.mainMenu()


if __name__ == "__main__":
    loginManager = LogManager()
    main = Main(loginManager)

    main.mainMenu()
