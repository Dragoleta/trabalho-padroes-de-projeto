from userLogState import LogManager
from userManager import UserManager


class LogIn:
    def makeLog(loginManager, filename):
        return LogIn.login(loginManager=loginManager, filename=filename)

    def login(loginManager, filename):
        name = str(input("Enter your username:"))
        password = str(input("Enter your password:"))
        user = UserManager.getUserFromJson(name, filename)

        if not user:
            print("User not found")
            return False

        if not user["password"] == password:
            print("Password incorrect")
            return False

        loginManager.login(name)
        print("Login successful ", name)
