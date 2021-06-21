from typing import List

from daos.reimbursement_dao import ReimbursementDAO
from entities.reimbursement import Reimbursement
from exceptions.reimbursement_not_found import ReimbursementNotFoundError
from services.reimbursement_service import ReimbursementService


class ReimbursementServiceImpl(ReimbursementService):
    def __init__(self, reimbursement_dao: ReimbursementDAO):
        self.reimbursement_dao: ReimbursementDAO = reimbursement_dao

    def create_reimbursement(self, employee_id: int, amount: float, description: str) -> Reimbursement:
        return self.reimbursement_dao.create_reimbursement(employee_id, amount, description)

    def get_reimbursement_by_id(self, r_id: int) -> Reimbursement:
        return self.reimbursement_dao.get_reimbursement_by_id(r_id)

    def get_reimbursements_by_employee(self, employee_id: int) -> List[Reimbursement]:
        return self.reimbursement_dao.get_reimbursements_by_employee(employee_id)

    def get_all_reimbursements(self) -> List[Reimbursement]:
        return self.reimbursement_dao.get_all_reimbursements()

    def approve_reimbursement(self, reimbursement: Reimbursement, message: str) -> Reimbursement:
        try:
            return self.reimbursement_dao.approve_reimbursement(reimbursement, message)
        except AttributeError:
            raise ReimbursementNotFoundError("Reimbursement does not exist. Please ensure you have the correct ID "
                                             "number.")

    def deny_reimbursement(self, reimbursement: Reimbursement, message: str) -> Reimbursement:
        try:
            return self.reimbursement_dao.deny_reimbursement(reimbursement, message)
        except AttributeError:
            raise ReimbursementNotFoundError("Reimbursement does not exist. Please ensure you have the correct ID "
                                             "number.")
