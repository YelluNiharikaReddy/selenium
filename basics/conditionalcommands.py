from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time



s = Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.facebook.com/login/")

driver.implicitly_wait(40)
time.sleep(3)

ele = driver.find_element(By.NAME , "email")
print(ele.is_displayed())
print(ele.is_enabled())
ele.send_keys("Niharikaprasanna@gmailcom")

ele1 = driver.find_element(By.NAME , "pass")
print(ele1.is_selected())
print(ele1.is_enabled())
print(ele1.is_selected())
ele1.send_keys("PradeepNiharika")
time.sleep(5)

driver.find_element(By.NAME , "login").click()
driver.quit()




