import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
#for dropdowns import select class and use its methods to select an option from the dropdown
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")
driver.maximize_window()
time.sleep(2)
#returns dropdown element(which contains multiple countries)
country_Dropdown = Select(driver.find_element(By.XPATH, "//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//p//select"))


time.sleep(3)
# select option from dropdown
country_Dropdown.select_by_visible_text("India")
#country_Dropdown.select_by_value("13")
country_Dropdown.select_by_index(13)
time.sleep(5)

#find number of all countries in the dropdown and names from for loop
allOptions = country_Dropdown.options
#or use xpath to find the country options

print("total number of countries", len(allOptions))
for i in allOptions:
    print(i.text)

#select option from without builtin select methods like select by value, visible, index
#driver.find_elements(By.XPATH, "")
for i in allOptions:
    if i.text == 'India':
        i.click()
        break

time.sleep(5)
driver.close()