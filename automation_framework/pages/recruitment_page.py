from selenium.webdriver.common.by import By
class RecruitmentPage:
    RECRUITMENT = (By.XPATH, "//span[text()='Recruitment']")
    
    def __init__(self, driver):
        self.driver = driver
        
    def test_recruitment(self):
        recruitment = self.driver.find_element(*self.DASHBOARDPAGE)
        assert dashboard.is_displayed() 