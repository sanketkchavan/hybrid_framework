
from selenium.webdriver.common.by import By

from base.webdriver_keywords import WebDriverKeywords


class LoginPage(WebDriverKeywords):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_username(self, username):
        # self.driver.find_element(By.NAME, "username").send_keys(username)
        self.type_by_locator((By.NAME, "username"), username)

    def enter_password(self, password):
        # self.driver.find_element(By.NAME, "password").send_keys(password)
        self.type_by_locator((By.NAME, "password"), password)

    def click_on_login(self):
        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        self.click_by_locator((By.XPATH, "//button[normalize-space()='Login']"))

    @property
    def get_invalid_error_message(self):
        return self.driver.find_element(By.XPATH, "//p[contains(normalize-space(),'Invalid')]").text

    @property
    def get_username_placeholder(self):
        return self.driver.find_element(By.NAME, "username").get_attribute("placeholder")

    @property
    def get_password_placeholder(self):
        return self.driver.find_element(By.NAME, "password").get_attribute("placeholder")