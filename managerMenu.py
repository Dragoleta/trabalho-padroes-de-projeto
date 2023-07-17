import subprocess

from passwordGen import PasswordGenerator
from passwordManager import PasswordManager
from userManager import UserManager


class ManagerMenu:
    def options(user, filename):
        passManager = PasswordManager()
        action = str(
            input(
                """
1 - add a password
2 - Show all saved passwords
3 - Filter passwords by site
4 - Go  back (press any key to return)
->"""
            )
        )

        match action:
            case "1":
                ManagerMenu.addPassword(passManager, filename, user)
            case "2":
                ManagerMenu.getPasswords(user, filename)
            case "3":
                ManagerMenu.filterPasswords(passManager, user, filename)

    def addPassword(passManager, filename, user):
        # call password generator
        subprocess.run(["clear"])
        siteName = str(input("Whats the site name? "))
        password = PasswordGenerator.menuPassGen()
        passManager.add_password(siteName, password)
        passManager.getAllPasswordsAndSave(filename, user)
        print("Password saved")
        ManagerMenu.options(user, filename)

    def getPasswords(user, filename):
        subprocess.run(["clear"])
        userFromJson = UserManager.getUserFromJson(user, filename)
        print(userFromJson["SavedPasswords"])
        ManagerMenu.options(user, filename)

    def filterPasswords(passManager, user, filename):
        try:
            subprocess.run(["clear"])
            siteName = str(input("Whats the site name? "))
            password = passManager.getPasswordFromSite(user, siteName, filename)
            print(password)
            ManagerMenu.options(user, filename)
        except:
            print("Site not found")
