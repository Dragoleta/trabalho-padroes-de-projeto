from userBuilder import UserBuilder
from userManager import UserManager


class SignIn:
    def getUserInfo():
        name = str(input("Choose your name: "))
        password = str(input("Choose your password: "))
        confPassword = str(input("Confirm your password: "))
        if not password or not name or not confPassword:
            print("Please enter all parameters")
            SignIn.getUserInfo()
        if not password == confPassword:
            print("Passwords must be equal")
            SignIn.getUserInfo()
        builder = UserBuilder()
        user = builder.set_name(name).set_password(password).build()
        return user

    def makeSign(filename):
        user = SignIn.getUserInfo()
        UserManager.saveUsersToJson(filename, user)
