import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from base.base_test import BaseTest 

class TestOrange(BaseTest):
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    def test_login(self):
        username = self.driver.find_element(*self.USERNAME)
        password = self.driver.find_element(*self.PASSWORD)
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        username.send_keys("Admin")
        password.send_keys("admin123")
        login_button.click()
        sleep(5)

