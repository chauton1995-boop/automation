from selenium.webdriver.common.by import By

class LoginPage:
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def test_login(self):
        username = self.driver.find_element(*self.USERNAME)
        password = self.driver.find_element(*self.PASSWORD)
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)

        username.send_keys("Admin")
        password.send_keys("admin123")
        login_button.click()