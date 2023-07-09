import random
import string


class PasswordBuilder:
    def __init__(self):
        self.password = None

    def generate_password(self):
        self.password = "".join(
            random.choices(string.ascii_letters + string.digits, k=8)
        )

    def get_password(self):
        return self.password
