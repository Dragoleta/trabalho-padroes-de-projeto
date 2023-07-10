import random
import string


class UserBuilder:
    def __init__(self):
        self.user = None
        self.password = None

    def generate_password(self, lenght):
       	self.name = str(input('Choose your username: '))
		password = str(input('Choose your password: '))
		confirmPass = str(input('Confirm your password: '))

		if password == confirmPass:
			self.password = confirmPass

    def get_user(self):
        return self.name, self.password
