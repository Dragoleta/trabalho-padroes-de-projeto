import random
import string


class PasswordBuilder:
    def __init__(self):
        self.password = None

    def generate_password(self, lenght):
        self.password = "".join(
            random.choices(string.ascii_letters + string.digits, k=lenght)
        )

    def get_password(self):
        return self.password
