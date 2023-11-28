import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://www.deadlinkcity.com/")

allLinks = driver.find_elements(By.TAG_NAME,"a")
count = 0

for link in allLinks:
    url = link.get_attribute('href')
    try:
        res = requests.head(url)
    except:
        None
    if res.status_code>=400:
        print("url is broken", url)
        count+=1
    else:
        print("not a broken link", url)

print("Total number of broken links", count)
