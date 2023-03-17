from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

"""Class contains all the selenium webdriver keywords """


class WebDriverKeywords:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 25)

    def click_by_locator(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator)).click()

    def type_by_locator(self, locator, text):
        self.wait.until(expected_conditions.visibility_of_element_located(locator)).send_keys(text)