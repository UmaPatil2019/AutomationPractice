import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demoqa.com/browser-windows")
time.sleep(3)
driver.maximize_window()

driver.find_element(By.XPATH,"//button[@id='windowButton']").click()
time.sleep(5)
driver.close() #closes the diver focused window only https://demoqa.com/browser-windows, but New browser window remains open
driver.quit() #closes all webdriver opened windows  driver opened window and new browser window, entire webdive seesion