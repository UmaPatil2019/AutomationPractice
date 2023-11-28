import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.support.ui import WebDriverWait as W
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://total-qa.com/checkbox-example/")
driver.maximize_window()
wait_time_out = 10



#select specific checkbox
# driver.find_element(By.XPATH, "//div[@id='primary']//input[1]").click()

#select multiple checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and @name='chk']")
print(len(checkboxes))
# for i in checkboxes:
#     print(i.click())

# #select some checkboxes not all
for i in range(len(checkboxes)):
    if i==2:
        checkboxes[i].click()

#select last two checkboxes
for i in range(len(checkboxes)-2, checkboxes):
    checkboxes[i].click()

#select first two checkboxes
for i in range(len(checkboxes)):
    if i<2:
        checkboxes[i].click()

#clear all the chkboxes
for i in checkboxes:
    if i.is_selected():
        i.click()

driver.close()
