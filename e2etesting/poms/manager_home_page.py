class ManagerHomePage:
    def __init__(self, driver):
        self.driver = driver

    def home_button(self):
        element = self.driver.find_element_by_id("home")
        return element

    def view_all_reimbursements(self):
        element = self.driver.find_element_by_id("view")
        return element

    def approve_or_deny_reimbursement(self):
        element = self.driver.find_element_by_id("approvedeny")
        return element

    def statistics(self):
        element = self.driver.find_element_by_id("statistics")
        return element
