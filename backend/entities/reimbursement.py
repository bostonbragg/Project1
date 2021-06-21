class Reimbursement:
    def __init__(self, r_id: int, employee_id: int, amount: float, description: str, status: str, message: str):
        self.r_id = r_id
        self.employee_id = employee_id
        self.amount = amount
        self.description = description
        # status messages are: Pending, Approved, Denied
        self.status = status
        self.message = message

    def as_json_dict(self):
        return {
            "reID": self.r_id,
            "employeeID": self.employee_id,
            "amount": self.amount,
            "description": self.description,
            "status": self.status,
            "message": self.message
        }