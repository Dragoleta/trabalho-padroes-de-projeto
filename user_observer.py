from abc import ABC, abstractmethod


class UserObserver(ABC):
    @abstractmethod
    def update(self, user):
        pass
    @abstractmethod
    def save(self, user):
    	pass
