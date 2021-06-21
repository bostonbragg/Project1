class ReimbursementNotFoundError(Exception):
    description: str = 'Occurs when a reimbursement is not found'

    def __init__(self, message: str):
        self.message = message
