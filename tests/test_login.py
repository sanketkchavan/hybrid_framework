import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By

from base.webdriver_listener import WebDriverWrapper
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utilities import data_source

"""Login related test cases """


class TestLogin(WebDriverWrapper):
    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_on_login()

        dashboard_page = DashboardPage(self.driver)
        assert_that("Dashboard").is_equal_to(dashboard_page.get_dashboard_header)

    @pytest.mark.parametrize("username, password, expected_error", data_source.test_invalid_login_data)
    def test_invalid_login(self, username, password, expected_error):
        login_page = LoginPage(self.driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_on_login()

        assert_that(expected_error).is_equal_to(login_page.get_invalid_error_message)


class TestLoginUI(WebDriverWrapper):
    def test_title(self):
        actual_title = self.driver.title
        assert_that("OrangeHRM").is_equal_to(actual_title)

    def test_header(self):
        actual_header = self.driver.find_element(By.XPATH, "//h5").text
        assert_that("Login").is_equal_to(actual_header)

    def test_login_placeholders(self):
        actual_username_placeholder = self.driver.find_element(By.NAME, "username").get_attribute("placeholder")
        actual_password_placeholder = self.driver.find_element(By.NAME, "password").get_attribute("placeholder")
        assert_that("Username").is_equal_to(actual_username_placeholder)
        assert_that("Password").is_equal_to(actual_password_placeholder)
