import json


class UserManager:
    def saveUsersToJson(filename, user):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        data[user.name] = {
            "password": user.password,
            "SavedPasswords": {},
        }

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def getUserFromJson(userName, filename):
        with open(filename, "r") as file:
            data = json.load(file)
        if userName in data:
            return data[userName]
        else:
            return None

    def getALLUsersFromJson(filename):
        with open(filename, "r") as file:
            data = json.load(file)

        if not data:
            return None

        return data
