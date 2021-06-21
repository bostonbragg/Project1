from abc import ABC, abstractmethod


class LoginDAO(ABC):

    @abstractmethod
    def login(self, username: str, password: str):
        pass
