import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service

s = Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
element = driver.find_element(By.XPATH , "//*[@id='HTML10']/div[1]/button")
action = ActionChains(driver)
action.double_click(element).perform()
time.sleep(5)