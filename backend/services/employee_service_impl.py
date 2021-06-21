from typing import List
from daos.employee_dao import EmployeeDAO
from entities.employee import Employee
from services.employee_service import EmployeeService


class EmployeeServiceImpl(EmployeeService):
    def __init__(self, employee_dao: EmployeeDAO):
        self.employee_dao: EmployeeDAO = employee_dao

    def get_employee(self, employee_id: int) -> Employee:
        return self.employee_dao.get_employee(employee_id)

    def get_all_employees(self) -> List[Employee]:
        return self.employee_dao.get_all_employees()
