from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
myWait = WebDriverWait(driver,10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException, Exception]) #explicit wait declaraion

#explicit wait effiectively works. Disadv; need to be called for multiple conditions
driver.get("https://www.google.com/")
searchBox = driver.find_element(By.NAME,"q")
searchBox.send_keys("Selenium")
searchBox.submit()
searchlink = myWait.until(EC.presence_of_element_located((By.XPATH,"//a[@href='https://www.selenium.dev/']//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='Selenium']")))
searchlink.click()
driver.close()

