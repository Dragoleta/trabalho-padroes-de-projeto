class PasswordGenerator:

#tirar o builder
    def __init__(self, builder, observers=None):
        self.builder = builder
        self.observers = observers or []

    def generate_password(self, lenght):
        self.builder.generate_password(lenght)
        password = self.builder.get_password()
        for observer in self.observers:
            observer.update(password)
