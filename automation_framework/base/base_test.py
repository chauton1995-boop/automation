import pytest       
from selenium import webdriver
from time import sleep

class BaseTest:
    @pytest.fixture(scope= 'class', autouse=True)
    def setup(self, request):
        #Headless mode round 9-11:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")  # Chạy trình duyệt ở chế độ headless
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        sleep(5)  # đợi trang load
        request.cls.driver = driver
        yield driver
        driver.quit()
    