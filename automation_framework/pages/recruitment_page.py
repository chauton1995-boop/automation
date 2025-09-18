from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from automation_framework.base.base_test import BaseTest

class RecruitmentPage(BaseTest):
    RECRUITMENT = (By.LINK_TEXT, "Recruitment")
    VACANCIES = (By.XPATH, "//a[text()='Vacancies']")
    ADDBUTTON = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
    VACANCYNAME = (By.XPATH, "//label[text()='Vacancy Name']/../following-sibling::div//input")
    JOBTITLE = (By.XPATH,"//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']")
    OPTION = (By.XPATH, "v")
    HIRINGMANAGER = (By.XPATH, "//input[@placeholder='Type for hints...']")
    SAVEBUTTON = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")

    def __init__(self, driver):
        self.driver = driver
        
    def vacancies(self, vacancy_name, job_title, hiring_manager):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.RECRUITMENT)).click()
        wait.until(EC.visibility_of_element_located(self.VACANCIES)).click()
        wait.until(EC.element_to_be_clickable(self.ADDBUTTON)).click()

        # Điền Vacancy Name
        wait.until(EC.presence_of_element_located(self.VACANCYNAME)).send_keys(vacancy_name)

        
        # Mở dropdown Job Title
        wait.until(EC.element_to_be_clickable(self.JOBTITLE)).click()

        # Đợi dropdown hiển thị option mong muốn
        option_xpath = (By.XPATH, f"//div[@role='option' and .='{job_title}']")
        wait.until(EC.visibility_of_element_located(option_xpath)).click()

        # Điền Hiring Manager
        wait.until(EC.presence_of_element_located(self.HIRINGMANAGER)).send_keys(hiring_manager)

        # Lưu lại
        wait.until(EC.element_to_be_clickable(self.SAVEBUTTON)).click()





        