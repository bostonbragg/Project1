class EmployeeHomePage:
    def __init__(self, driver):
        self.driver = driver

    def home_button(self):
        element = self.driver.find_element_by_id("home")
        return element

    def submit_reimbursement(self):
        element = self.driver.find_element_by_id("submit")
        return element

    def view_reimbursements(self):
        element = self.driver.find_element_by_id("view")
        return element

    def logout(self):
        element = self.driver.find_element_by_id("logout")
        return element
