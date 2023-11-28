import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.snapdeal.com/")
driver.get("https://www.amazon.com/")

driver.back() #snapdeal opens
time.sleep(3)
driver.forward() #amzon opens
time.sleep(5)

driver.refresh() #refreshes amazon page
driver.quit()