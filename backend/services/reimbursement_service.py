from abc import ABC, abstractmethod
from typing import List
from entities.reimbursement import Reimbursement


class ReimbursementService(ABC):
    @abstractmethod
    def create_reimbursement(self, employee_id: int, amount: int, description: str) -> Reimbursement:
        pass

    @abstractmethod
    def get_reimbursement_by_id(self, r_id: int) -> Reimbursement:
        pass

    @abstractmethod
    def get_reimbursements_by_employee(self, employee_id: int) -> List[Reimbursement]:
        pass

    @abstractmethod
    def get_all_reimbursements(self) -> List[Reimbursement]:
        pass

    @abstractmethod
    def approve_reimbursement(self, reimbursement: Reimbursement, message: str) -> Reimbursement:
        pass

    @abstractmethod
    def deny_reimbursement(self, reimbursement: Reimbursement, message: str) -> Reimbursement:
        pass
