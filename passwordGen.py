import random
import string


class PasswordGenerator:
    def generate_password(chars, length):
        return "".join(random.choice(chars) for _ in range(length))

    def passwordGenerator(func):
        def wrapper(*args, **kwargs):
            password = func(*args, **kwargs)
            return password

        return wrapper

    @passwordGenerator
    def generate_simple_password(length):
        chars = string.ascii_lowercase + string.digits
        return PasswordGenerator.generate_password(chars, length)

    @passwordGenerator
    def generate_complex_password(length):
        chars = string.ascii_lowercase + string.digits + string.punctuation
        return PasswordGenerator.generate_password(chars, length)

    @passwordGenerator
    def generate_super_password(length):
        length = length * 2
        chars = (
            string.ascii_lowercase
            + string.digits
            + string.punctuation
            + string.ascii_uppercase
        )
        return PasswordGenerator.generate_password(chars, length)

    def menuPassGen():
        action = input(
            """How strong will your password be?
        1 - strong 2 - very strong 3 - superman strong
    ->"""
        )

        length = int(
            input(
                """Want to specify a length for your password?
    Enter a number between 8 and 30: """
            )
        )

        if length < 8 or length > 30:
            length = 15

        match action:
            case "1":
                return PasswordGenerator.generate_simple_password(length)
            case "2":
                return PasswordGenerator.generate_complex_password(length)
            case "3":
                return PasswordGenerator.generate_super_password(length)
