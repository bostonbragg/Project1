from abc import abstractmethod, ABC
from typing import List
from entities.employee import Employee


class EmployeeDAO(ABC):

    @abstractmethod
    def get_employee(self, employee_id: int) -> Employee:
        pass

    @abstractmethod
    def get_all_employees(self) -> List[Employee]:
        pass
