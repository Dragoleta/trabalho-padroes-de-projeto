from abc import ABC, abstractmethod


class PasswordObserver(ABC):
    @abstractmethod
    def update(self, password):
        pass
