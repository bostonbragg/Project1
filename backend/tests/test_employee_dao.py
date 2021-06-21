from daos.employee_dao_postgres import EmployeeDAOPostgres

dao = EmployeeDAOPostgres()


def test_get_employee():
    test_id = 1
    employee = dao.get_employee(test_id)
    assert employee.employee_id == test_id


def test_get_all_employees():
    employees = dao.get_all_employees()
    assert employees[0].employee_id == 1