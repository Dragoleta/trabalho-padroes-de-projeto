class PasswordGenerator:
    def __init__(self, builder, observers=None):
        self.builder = builder
        self.observers = observers or []

    def generate_password(self):
        self.builder.generate_password()
        password = self.builder.get_password()
        for observer in self.observers:
            observer.update(password)
