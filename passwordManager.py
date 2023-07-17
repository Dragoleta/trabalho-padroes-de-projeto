import json

from passwordBuilder import PasswordBuilder
from userManager import UserManager


class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def add_password(self, siteName, sitePassword):
        builder = PasswordBuilder()
        newPassword = (
            builder.set_siteName(siteName).set_sitePassword(sitePassword).build()
        )
        self.passwords[siteName] = newPassword

    def getAllPasswordsAndSave(
        self,
        filename,
        userName,
    ):
        data = UserManager.getALLUsersFromJson(filename)

        for password in self.passwords.values():
            data[userName]["SavedPasswords"][password.siteName] = (
                str(password.sitePassword),
            )

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def getPasswordFromSite(self, user, siteName, filename):
        user = UserManager.getUserFromJson(user, filename)
        return f"""{siteName}: { user["SavedPasswords"][siteName]}"""

    # todo
    def updatePassword(self, user, siteName, password, filename):
        pass
