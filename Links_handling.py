from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demo.nopcommerce.com/")

#click on internal link(link that navigates within the application)
driver.find_element(By.LINK_TEXT,"Digital downloads").click()

#find number of links in the webpage
links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))

#print all links
for i in links:
    print(i.text)



driver.close