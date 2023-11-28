from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()
#isdiplayed #isdisplayed, #isenabled(to check status of checkbox/radio buttons)
SearchBox=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("Is displayed: " , SearchBox.is_displayed())
print("Is enabled: ", SearchBox.is_enabled())
#before selecting radio button
rb_male = driver.find_element(By.XPATH,"//input[@id='gender-male']")
print(rb_male.is_selected())

rb_female = driver.find_element(By.XPATH,"//input[@id='gender-female']")
print(rb_female.is_selected())

#after selecting female radio button
rb_female.click()
print(rb_female.is_selected())
print(rb_male.is_selected())

driver.close()
