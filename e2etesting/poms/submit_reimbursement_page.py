from selenium.webdriver.remote.webelement import WebElement


class SubmitReimbursementPage:
    def __init__(self, driver):
        self.driver = driver

    def amount(self):
        element: WebElement = self.driver.find_element_by_id("amount")
        return element

    def description(self):
        element: WebElement = self.driver.find_element_by_id("description")
        return element

    def submit(self):
        element: WebElement = self.driver.find_element_by_id("submit")
        return element
