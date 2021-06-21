from abc import ABC, abstractmethod


class LoginService(ABC):
    @abstractmethod
    def login(self, username: str, password: str):
        pass
