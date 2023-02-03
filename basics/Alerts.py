from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(By.XPATH , "//*[@id='HTML9']/div[1]/button").click()
time.sleep(5)
#driver.switch_to.alert.accept()  # close the alert window by clicking ok button
#time.sleep(5)
driver.switch_to.alert.dismiss()  # close the alert window by using cancle buttton
time.sleep(5)
driver.quit()