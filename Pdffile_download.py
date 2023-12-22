import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import os
location = os.getcwd() # returns current working directory, instead of hardcoding the location an object is created with the method getcwd()

def chrome_setup1():
    #to download a file in desired location preferences object is created, instead of downloading in default downloads folder
    preferences = {"download.default_directory": location, "plugins.always_open_pdf_externally":True}
    options_obj = webdriver.ChromeOptions()
    #options_obj.add_argument("--disable--notifications")
    options_obj.add_experimental_option("prefs", preferences)

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options_obj)
    return driver

driver1 = chrome_setup1()
driver1.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")
#driver1.maximize_window()
driver1.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]").click()
time.sleep(10)