from daos.login_dao import LoginDAO
from utils.connection_util import connection


class LoginDAOPostgres(LoginDAO):
    def login(self, username: str, password: str):
        sql = """select pwd, employee_id from employee where username = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [str(username)])
        try:
            sql_return = cursor.fetchall()[0]
            attempted_password = sql_return[0]
            employee_id = sql_return[1]
            e_or_m = employee_or_manager(employee_id)

            output = {"responseMessage": "", "employeeID": employee_id, "employeeOrManager": e_or_m}

            if attempted_password == password:
                output["responseMessage"] = "Login successful"
                return output
            else:
                output["responseMessage"] = "Login failed"
                output["employeeID"] = ""
                return output

        except (TypeError, IndexError):
            return {"responseMessage": "Username does not exist"}


def employee_or_manager(employee_id: int) -> str:
    sql = """select is_manager from employee where employee_id = %s"""
    cursor = connection.cursor()
    cursor.execute(sql, [str(employee_id)])
    is_manager = cursor.fetchone()[0]
    if is_manager:
        return "Manager"
    elif not is_manager:
        return "Employee"
    else:
        return str(is_manager)
