import pytest       
from selenium import webdriver
from time import sleep
from utils.config_reader import ConfigReader
class BaseTest:
    @pytest.fixture(scope= 'class', autouse=True)
    def setup(self, request):
        #Headless mode round 9-11:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")  # Chạy trình duyệt ở chế độ headless
        driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        sleep(5)  # đợi trang load
        
      
         
        # Attach to the test class to sue self.driver in test class
        request.cls.driver = driver
        #Teardown
        yield self.driver
        self.driver.quit()
    