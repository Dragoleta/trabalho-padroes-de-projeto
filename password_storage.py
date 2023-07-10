from password_observer import PasswordObserver


class PasswordStorage(PasswordObserver):
    def update(self, password):
        with open("passwords.txt", "a") as file:
            file.write(f"{password}\n")	
