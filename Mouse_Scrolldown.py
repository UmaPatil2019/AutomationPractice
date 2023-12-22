import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

#scroll down page by pixel by using javascript
driver.execute_script("window.scrollBy(0,2000)", "")
value1 = driver.execute_script("return window.pageYOffset;")
print("value of pixels moved:", value1)
time.sleep(2)

#scroll down page until element visible
flag = driver.find_element(By.XPATH, "//img[@alt='Flag of India']")
driver.execute_script("arguments[0].scrollIntoView();",flag)
value2 = driver.execute_script("return window.pageYOffset;")
print("number of pixels scrolled: ", value2)
time.sleep(2)

#scroll down until end of page
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)","")
value3 = driver.execute_script("return window.pageYOffset;")
print("number of pixels scrolled: ", value3)
time.sleep(2)

#scroll back to top of page
driver.execute_script("window.scrollBy(0, -document.body.scrollHeight)","")
value4 = driver.execute_script("return window.pageYOffset;")
print("number of pixels scrolled: ", value4)
time.sleep(3)