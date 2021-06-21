from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver

    def username(self) -> WebElement:
        element: WebElement = self.driver.find_element_by_id("username")
        return element

    def password(self) -> WebElement:
        element: WebElement = self.driver.find_element_by_id("password")
        return element

    def login_button(self) -> WebElement:
        element: WebElement = self.driver.find_element_by_id("loginButton")
        return element
