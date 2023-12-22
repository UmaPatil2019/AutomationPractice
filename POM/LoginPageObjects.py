from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class LoginPage:
    #Locators
    txtbox_username_id = "Email"
    txtbox_password_id = "Password"
    button_login_xpath = "//button[normalize-space()='Log in']"

    #constructor
    def __init__(self,driver):
        self.driver = driver

    #Action methods
    def setUserName(self, name):
        username = self.driver.find_element(By.ID, self.txtbox_username_id)
        username.clear()
        username.send_keys(name)


    def setPassword(self, pwd):
        password = self.driver.find_element(By.ID, self.txtbox_password_id)
        password.clear()
        password.send_keys(pwd)


    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()



