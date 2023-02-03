from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

s = Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.instagram.com/")

driver.implicitly_wait(10)

ele = driver.find_element(By.NAME , "username")
ele.clear()
ele.send_keys("Yellu_niharika_reddy")

ele1 = driver.find_element(By.XPATH , "//*[@id='loginForm']/div/div[2]/div/label/input")
ele1.clear()
ele1.send_keys("prasanna@1997")
driver.find_element(By.XPATH , "//*[@id='loginForm']/div/div[2]/div/div/div/button").click()

time.sleep(10)
driver.find_element(By.XPATH , "//*[@id='loginForm']/div/div[3]/button/div").click()

driver.quit()