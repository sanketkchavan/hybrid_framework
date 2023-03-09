from selenium.webdriver.common.by import By


class TestValidEmployee:

    def test_add_valid_employee(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Login')]").click()
        self.driver.find_element(By.XPATH, "//span[text()='PIM']").click()
        self.driver.find_element(By.XPATH, "//li/a[text()='Add Employee']").click()
        self.driver.find_element(By.NAME, "firstName").send_keys("John")
        self.driver.find_element(By.NAME, "middleName").send_keys("k")
        self.driver.find_element(By.NAME, "lastName").send_keys("wick")
        self.driver.find_element(By.XPATH, "//button[@type='submit']")

