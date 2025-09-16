from time import sleep
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver
        
    def login(self, username, password):
        self.get_element(self.USERNAME).send_keys(username)
        self.get_element(self.PASSWORD).send_keys(password)
        self.get_element(self.LOGIN_BUTTON).click()
        sleep(5)  
          
    # def test_login(self):
    #     username = self.driver.find_element(*self.USERNAME)
    #     password = self.driver.find_element(*self.PASSWORD)
    #     login_button = self.driver.find_element(*self.LOGIN_BUTTON)
    #     username.send_keys("Admin")
    #     password.send_keys("admin123")
    #     login_button.click()
    #     sleep(5)




