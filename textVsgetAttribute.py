from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.saucedemo.com/")
username = driver.find_element(By.ID,"user-name")
username.clear()
username.send_keys("standard_user")
print(username.text) #returns oiiner label of username tag in html, here it doesnt exist, hence nothing returned
print(username.get_attribute("type")) #returns value of any html attibute for username tag , ex; name="username", id="username"

