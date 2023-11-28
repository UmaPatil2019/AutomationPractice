from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Url_Launcher():
   def appln_login(self):
      driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
      driver.get("https://www.target.com/")
      driver.maximize_window()
      print(driver.title)
      driver.close()


object = Url_Launcher()
object.appln_login()