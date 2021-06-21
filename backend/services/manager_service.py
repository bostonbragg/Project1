from abc import ABC, abstractmethod
from typing import List


class ManagerService(ABC):
    @abstractmethod
    def get_highest_total_for_an_employee(self) -> List[dict]:
        pass

    @abstractmethod
    def get_highest_by_status(self, status: str) -> List[dict]:
        pass

    @abstractmethod
    def get_mean_by_status(self, status: str) -> dict:
        pass

    @abstractmethod
    def get_most_by_employee_by_status(self, status: str) -> dict:
        pass
