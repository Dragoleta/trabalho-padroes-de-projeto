import subprocess

from loginSystem import LogIn
from signinSystem import SignIn
from userLogState import LogManager


class MenuLog:
    def menu(loginManager, filename):
        action = str(
            input(
                """    
Press 1 to login
Press 2 to SignUp
->"""
            )
        )

        match action:
            case "1":
                subprocess.run(["clear"])

                return LogIn.makeLog(loginManager=loginManager, filename=filename)

            case "2":
                subprocess.run(["clear"])
                SignIn.makeSign(filename)
                MenuLog.menu(loginManager, filename)
            case _:
                subprocess.run(["clear"])
                print("Must be an number between 1 and 2")
                MenuLog.menu(loginManager, filename)
