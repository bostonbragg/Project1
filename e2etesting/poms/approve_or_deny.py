from selenium.webdriver.support.select import Select


class ApproveOrDeny:
    def __init__(self, driver):
        self.driver = driver

    def reimbursement_id(self):
        element = self.driver.find_element_by_id("reimbursementID")
        return element

    def approve_or_deny(self):
        element = Select(self.driver.find_element_by_id("approveOrDeny"))
        return element

    def message(self):
        element = self.driver.find_element_by_id("message")
        return element

    def submit(self):
        element = self.driver.find_element_by_id("submit")
        return element

    def message_after_submit(self):
        element = self.driver.find_element_by_id("messageaftersubmit")
