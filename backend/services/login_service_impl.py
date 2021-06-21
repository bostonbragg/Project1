from daos.login_dao import LoginDAO
from services.login_service import LoginService


class LoginServiceImpl(LoginService):
    def __init__(self, login_dao):
        self.login_dao: LoginDAO = login_dao

    def login(self, username: str, password: str):
        return self.login_dao.login(username, password)
