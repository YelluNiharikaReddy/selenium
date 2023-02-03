from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

s=Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

drag = driver.find_element(By.XPATH,"//*[@id='draggable']")
target = driver.find_element(By.XPATH,"//*[@id='droppable']")
action = ActionChains(driver)
action.drag_and_drop(drag,target).perform()
