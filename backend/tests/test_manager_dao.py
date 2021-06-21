from daos.manager_dao_postgres import ManagerDAOPostgres
from daos.reimbursement_dao_postgres import ReimbursementDAOPostgres
from entities.reimbursement import Reimbursement

manager_dao = ManagerDAOPostgres()
reimbursement_dao = ReimbursementDAOPostgres()


def test_get_highest_total_for_an_employee():
    employee_id = 1
    test_r = Reimbursement(-1, employee_id, 99999999999999, "Absurdly high", "", "")
    created_r = reimbursement_dao.create_reimbursement(employee_id, test_r.amount, test_r.message)
    test_r = Reimbursement(created_r.employee_id, test_r.employee_id, test_r.amount, test_r.description, "", "")
    reimbursement_dao.approve_reimbursement(test_r, "")
    employee_list = manager_dao.get_highest_total_for_an_employee()
    employee: dict = employee_list[0]
    assert employee.get("employeeID") == employee_id


def test_get_highest_by_status():
    reimbursement_list = manager_dao.get_highest_by_status("Pending")
    reimbursement = reimbursement_list[0]
    assert reimbursement["reID"] == 3


def test_get_mean_by_status():
    reimbursement = reimbursement_dao.create_reimbursement(1, 200, "testing things")
    reimbursement_dao.approve_reimbursement(reimbursement, "Hmm ok")
    mean = manager_dao.get_mean_by_status("Approved")
    assert mean["amount"] == 150
