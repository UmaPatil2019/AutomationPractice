from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from LoginPageObjects import LoginPage

class TestLogin:
    def test_Login(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://admin-demo.nopcommerce.com/login")
        self.driver.maximize_window()

        self.loginpage = LoginPage(self.driver)
        self.loginpage.setUserName("admin@yourstore.com")
        self.loginpage.setPassword("admin")
        self.loginpage.clickLogin()
        self.actual_title = self.driver.title
        self.driver.close()
        assert self.actual_title == "Dashboard / nopCommerce administration"