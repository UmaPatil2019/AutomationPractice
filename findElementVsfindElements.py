from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#diff bet findElements and FindElements
# find ele returns single ele, send keys method avaialble, throws exception whent
# that ele not available in the application.
# find eles returns multiple eles, send keys method not avaialble, doesnot thrw exception whent
# that ele not available in the application, instead len returns as 0

#findelement
driver.get("https://demo.nopcommerce.com/")
single_element = driver.find_element(By.ID,"small-searchterms").send_keys("mac")

multiple_elements = driver.find_element(By.XPATH,"//div[@class='footer']//a")
print(multiple_elements.text) # returns first element only from multiple list of items

#ele_NotAvailable = driver.find_element(By.LINK_TEXT,"Log").click() #throws exception as "no such element: Unable to locate element:" as Log element is not found, instead its Log in in the application
#print(len(ele_NotAvailable))

#find Elements
single_element = driver.find_elements(By.ID,"small-searchterms")
print(len(single_element))
single_element[0].send_keys("mac")

multiple_elements = driver.find_elements(By.XPATH,"//div[@class='footer']//a")
for i in multiple_elements:
    print((i.text))

ele_NotAvailable = driver.find_elements(By.LINK_TEXT,"Log") #doesn't throw exception instead returns element returned as : 0
print(len(ele_NotAvailable))
driver.close()