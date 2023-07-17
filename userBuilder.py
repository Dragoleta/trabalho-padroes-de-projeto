class User:
    def __init__(self):
        self.name = None
        self.password = None


class UserBuilder:
    def __init__(self):
        self.user = User()

    def set_name(self, name):
        self.user.name = name
        return self

    def set_password(self, password):
        self.user.password = password
        return self

    def build(self):
        return self.user

