class Employee:
    def __init__(self, employee_id: int, first_name: str, last_name: str, manager_id: int, username: str, pwd: str):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.manager_id = manager_id
        self.username = username
        self.password = pwd

    def as_json_dict(self):
        return {
            "employeeID": self.employee_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "managerID": self.manager_id,
            "username": self.username,
            "password": self.password
        }