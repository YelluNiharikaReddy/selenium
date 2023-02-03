from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.ivolunteer.in/volunteer-sign-up")
driver.implicitly_wait(10)
status = driver.find_element(By.XPATH , "//*[@id='page-layout-805']").click()
print(status)

