from selenium.webdriver.common.by import By
class DashboardPage:
    DASHBOARDPAGE = (By.XPATH, "//h6[text()='Dashboard']")
    
    def __init__(self, driver):
        self.driver = driver
        
    def is_dashboard_displayed(self):
        dashboard = self.driver.find_element(*self.DASHBOARDPAGE)
        return dashboard.is_displayed()
        