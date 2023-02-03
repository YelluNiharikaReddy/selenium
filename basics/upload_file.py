from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
import time


s = Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

driver.switch_to.frame(0)

driver.find_element(By.XPATH , "//*[@id='RESULT_FileUpload-10']").send_keys("C://Users/Dell/Desktop/desktop/pic 2.jpg")

driver.close()
