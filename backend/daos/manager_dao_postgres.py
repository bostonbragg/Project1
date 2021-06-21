from typing import List
from daos.manager_dao import ManagerDAO
from utils.connection_util import connection


class ManagerDAOPostgres(ManagerDAO):
    def get_highest_total_for_an_employee(self) -> List[dict]:
        sql = """select employee.employee_id, first_name, last_name, sum(amount) as total_cost 
                from employee, reimbursement
                where employee.employee_id = reimbursement.employee_id and reimbursement.status = 'Approved'
                group by employee.employee_id
                having sum(amount) = (
                        select sum(amount)
                        from employee, reimbursement
                        where employee.employee_id = reimbursement.employee_id and reimbursement.status = 'Approved'
                        group by employee.employee_id
                        order by sum(amount) desc limit 1
                    )"""
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        employee_list = []
        for employees in records:
            attributes = {"employeeID": employees[0], "firstName": employees[1], "lastName": employees[2],
                          "amount": employees[3]}
            employee_list.append(attributes)
        return employee_list

    def get_highest_by_status(self, status: str) -> List[dict]:
        if str(status) == "Overall":
            sql = """select r.*, e.first_name, e.last_name 
                    from reimbursement as r, employee as e
                    where r.employee_id = e.employee_id 
                    order by amount desc limit 1
                  """
            cursor = connection.cursor()
            cursor.execute(sql)
        else:
            sql = """select r.*, e.first_name, e.last_name 
                    from reimbursement as r, employee as e
                    where status = %s and r.employee_id = e.employee_id 
                    order by amount desc limit 1
                   """
            cursor = connection.cursor()
            cursor.execute(sql, [str(status)])

        records = cursor.fetchall()
        reimbursement_list = []
        for reimbursements in records:
            attributes = {"reID": reimbursements[0], "employeeID": reimbursements[1], "amount": reimbursements[2],
                          "description": reimbursements[3], "status": reimbursements[4], "message": reimbursements[5],
                          "firstName": reimbursements[6], "lastName": reimbursements[7]}
            reimbursement_list.append(attributes)
        return reimbursement_list

    def get_mean_by_status(self, status: str) -> dict:
        if str(status) == "Overall":
            sql = """select avg(amount)
                    from reimbursement"""
            cursor = connection.cursor()
            cursor.execute(sql)
        else:
            sql = """select avg(amount)
                    from reimbursement
                    where status = %s"""
            cursor = connection.cursor()
            cursor.execute(sql, [str(status)])

        amount = cursor.fetchone()[0]
        return {"amount": amount}
