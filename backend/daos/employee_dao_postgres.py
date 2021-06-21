from typing import List
from daos.employee_dao import EmployeeDAO
from entities.employee import Employee
from utils.connection_util import connection


class EmployeeDAOPostgres(EmployeeDAO):
    def get_employee(self, employee_id: int) -> Employee:
        sql = """select * from employee where employee_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, (str(employee_id)))
        records = cursor.fetchall()
        for employee_parts in records:
            employee = Employee(employee_parts[0], employee_parts[1], employee_parts[2], employee_parts[3],
                                employee_parts[4], employee_parts[5])
            return employee

    def get_all_employees(self) -> List[Employee]:
        sql = """select * from employee order by employee_id"""
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        employee_list = []
        for employee_parts in records:
            employee = Employee(employee_parts[0], employee_parts[1], employee_parts[2], employee_parts[3],
                                employee_parts[4], employee_parts[5])
            employee_list.append(employee)
        return employee_list
