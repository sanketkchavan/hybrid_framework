import pytest
from selenium import webdriver
from assertpy import assert_that
from selenium.webdriver.common.by import By
from base.webdriver_listener import WebDriverWrapper

from utilities import data_source


class TestLogin:
    @pytest.fixture(scope="function", autouse=True)
    def browser_config(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        yield
        self.driver.quit()


class TestLogin(WebDriverWrapper):

    def test_valid_login(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Login')]").click()
        actual_text = self.driver.find_element(By.XPATH, "//h6[contains(normalize-space(),'Dashboard')]").text
        assert_that("Dashboard").is_equal_to(actual_text)

    @pytest.mark.parametrize("username, password, expected_error", data_source.test_invalid_login)
    def test_invalid_login(self, username, password, expected_error):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        actual_error = self.driver.find_element(By.XPATH, "//p[contains(normalize-space() ,'Invalid')]").text
        assert_that(expected_error).is_equal_to(actual_error)


class TestLoginUI:
    @pytest.fixture(scope="function", autouse=True)
    def browser_config(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        yield
        self.driver.quit()

    def test_title(self):
        actual_title = self.driver.title
        assert_that("OrangeHRM").is_equal_to(actual_title)

    def test_header(self):
        actual_header = self.driver.find_element(By.XPATH, "//h5").text
        assert_that("Login").is_equal_to(actual_header)

    def test_login_placeholder(self):
        actual_username_placeholder = self.driver.find_element(By.NAME, "username").get_attribute("Placeholder")
        actual_password_placeholder = self.driver.find_element(By.NAME, "password").get_attribute("Placeholder")
        assert_that("Username").is_equal_to(actual_username_placeholder)
        assert_that("Password").is_equal_to(actual_password_placeholder)
