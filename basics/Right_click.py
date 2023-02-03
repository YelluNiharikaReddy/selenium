import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

s= Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

button = driver.find_element(By.ID,"context-menu-layer")
action = ActionChains(driver)
action.context_click(button).perform()
time.sleep(5)