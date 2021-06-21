class Statistics:
    def __init__(self, driver):
        self.driver = driver

    def highest_employee(self):
        element = self.driver.find_element_by_id("highest-employee-tab")
        return element

    def highest_status(self):
        element = self.driver.find_element_by_id("highest-status-tab")
        return element

    def mean(self):
        element = self.driver.find_element_by_id("mean-tab")
        return element
