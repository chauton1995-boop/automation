import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from base.base_test import BaseTest
from pages.login_page import LoginPage   # ✅ import LoginPage
from pages.dashboard_page import DashboardPage

class TestOrange(BaseTest):
    
    def test_login(self):
        loginpage = LoginPage(self.driver)
        loginpage.test_login()
        dashboardpage = DashboardPage(self.driver)
        assert dashboardpage.is_dashboard_displayed() is True
        sleep(5)