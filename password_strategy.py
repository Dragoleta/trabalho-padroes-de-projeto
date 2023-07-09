from abc import ABC, abstractmethod


class PasswordStrategy(ABC):
    @abstractmethod
    def generate_password(self):
        pass
