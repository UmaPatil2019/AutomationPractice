import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#dynamic table

class WebTable2():
    def Table2(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))