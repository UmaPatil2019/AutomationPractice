# Two types of loacators
# Locators; id, name, linktext, partiallinktext, classname, tagname
# Customized loacators css selector and xpath
# Types of css selectors; tag&id, tag&class, tag&attribute, tag&class&attribute
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH,("//button[@type='submit']")).click()
time.sleep(3)
#driver.find_element(By.ID,"")
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()

#class name and tag names are same for multiple elements
length = driver.find_elements(By.CLASS_NAME,"orangehrm-dashboard-widget-body")
print(len(length))
time.sleep(3)
driver.find_element(By.PARTIAL_LINK_TEXT, "Inc").click()
time.sleep(3)

driver.maximize_window()
time.sleep(3)

driver.close()