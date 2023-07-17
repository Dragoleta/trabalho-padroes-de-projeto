from abc import ABC, abstractmethod


class LogState(ABC):
    @abstractmethod
    def login(self, username):
        pass

    @abstractmethod
    def logout(self):
        pass
