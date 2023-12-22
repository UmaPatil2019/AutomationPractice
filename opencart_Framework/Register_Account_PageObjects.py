from selenium.webdriver.common.by import By

class RegisterPage:
    #Locators
    FirstName_id = "input-firstname"
    LastName_id = "input-lastname"
    Email_id = "input-email"
    Password_id = "input-password"
    Newsletter_xpath = "//label[normalize-space()='No']"
    PrivacyPolicy_xpath = "//input[@type='checkbox']"
    Continue_xpath = "//button[@type='submit']"

    #constructor
    def __init__(self, driver):
        self.driver = driver

    #Action Methods
    def setFirstName(self, Fname):
        FirstName = self.driver.find_element(By.ID, self.FirstName_id)
        FirstName.clear()
        FirstName.send_keys(Fname)

    def setLastName(self, Lname):
        LastName = self.driver.find_element(By.ID, self.LastName_id)
        LastName.clear()
        LastName.send_keys(Lname)

    def setEmail(self, email):
        Email = self.driver.find_element(By.ID, self.Email_id)
        Email.clear()
        Email.send_keys(email)

    def setPassword(self, pwd):
        Password = self.driver.find_element(By.ID, self.Password_id)
        Password.clear()
        Password.send_keys(pwd)

    def NewsLetter_RadioButton(self):
        newsletter = self.driver.find_element(By.XPATH, self.Newsletter_xpath)
        newsletter.click()

    def Privacy_CheckBox(self):
        PrivacyPolicy = self.driver.find_element(By.XPATH, self.PrivacyPolicy_xpath)
        PrivacyPolicy.click()

    def Continue_Button(self):
        submit = self.driver.find_element(By.XPATH, self.Continue_xpath)
        submit.click()

















