from user_observer import UserObserver


class UserStorage(UserObserver):
    def save(self, user):
        with open("users.txt", "a") as file:
            file.write(f"{user}\n")
