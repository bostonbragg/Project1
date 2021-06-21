class EmployeeViewReimbursements:
    def __init__(self, driver):
        self.driver = driver

    def reimbursements(self):
        element = self.driver.find_element_by_id("reimbursements")
        return element
