from password_builder import PasswordBuilder
from password_generator import PasswordGenerator
from password_storage import PasswordStorage
from password_strategy import PasswordStrategy


class ComplexPasswordStrategy(PasswordStrategy):
    def generate_password(self):
        builder = PasswordBuilder()
        generator = PasswordGenerator(builder)
        storage = PasswordStorage()
        generator.observers.append(storage)

        # Add additional complexity to the password generation logic
        builder.generate_password()
        password = builder.get_password()
        complex_password = password + "!$#"
        builder.password = complex_password

        generator.generate_password()
