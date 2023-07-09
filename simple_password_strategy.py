from password_builder import PasswordBuilder
from password_generator import PasswordGenerator
from password_storage import PasswordStorage
from password_strategy import PasswordStrategy


class SimplePasswordStrategy(PasswordStrategy):
    def generate_password(self):
        builder = PasswordBuilder()
        generator = PasswordGenerator(builder)
        storage = PasswordStorage()
        generator.observers.append(storage)
        generator.generate_password()
