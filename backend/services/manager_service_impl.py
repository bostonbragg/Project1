from typing import List
from daos.manager_dao import ManagerDAO
from services.manager_service import ManagerService


class ManagerServiceImpl(ManagerService):
    def __init__(self, manager_dao: ManagerDAO):
        self.manager_dao = manager_dao

    def get_highest_total_for_an_employee(self) -> List[dict]:
        return self.manager_dao.get_highest_total_for_an_employee()

    def get_highest_by_status(self, status: str) -> List[dict]:
        return self.manager_dao.get_highest_by_status(status)

    def get_mean_by_status(self, status: str) -> dict:
        return self.manager_dao.get_mean_by_status(status)

    def get_most_by_employee_by_status(self, status: str) -> dict:
        pass
