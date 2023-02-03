from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
driver.get("https://www.youtube.com/")
driver.get("https://mail.google.com/mail/u/0/#inbox")
print(driver.title)
driver.back()
print(driver.title)
driver.forward()
print(driver.title)
driver.close()

