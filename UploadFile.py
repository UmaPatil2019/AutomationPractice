import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
driver.find_element(By.XPATH, "//input[@class='input-file']").send_keys("/Users/maheshpatil/Downloads/selenium_python_sdet_sample_template (1).docx")
time.sleep(5)
