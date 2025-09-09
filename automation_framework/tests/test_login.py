import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def test_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    sleep(2)  # đợi trang load

    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    username.send_keys("Admin")
    password.send_keys("admin123")
    login_button.click()

    sleep(5)
    driver.quit()