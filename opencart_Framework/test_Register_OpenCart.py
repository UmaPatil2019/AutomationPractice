import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Register_Account_PageObjects import RegisterPage

class Test_RegisterPage:
    def test_RegisterPage(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://demo.opencart.com/index.php?route=account/register&language=en-gb")
        self.driver.maximize_window()

        self.register = RegisterPage(self.driver)
        self.register.setFirstName("abc")
        self.register.setLastName("xyz")
        self.register.setEmail("abcdef@gmail.com")
        self.register.setPassword("admin")
        self.register.NewsLetter_RadioButton()
        self.register.Privacy_CheckBox()
        time.sleep(5)
        self.register.Continue_Button()
        self.driver.close()