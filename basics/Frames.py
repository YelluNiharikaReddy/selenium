from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s = Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

driver.switch_to.frame("packageListFrame")                   # paste name of first frame
driver.find_element(By.XPATH,"/html/body/main/ul/li[4]/a").click()
time.sleep(5)

driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")                   ## paste name of second frame
driver.find_element(By.XPATH , "/html/body/main/ul/li[8]/a").click()


driver.switch_to.default_content()
time.sleep(5)

driver.switch_to.frame("classFrame")                         # paste the name of 3rd frame
driver.find_element(By.XPATH , "//*[@id='i3']/th/a").click()
time.sleep(5)
