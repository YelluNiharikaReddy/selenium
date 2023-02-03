from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s=Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.amazon.in/")
driver.save_screenshot("C:/Users/Dell/Desktop/New folder/home.png")
driver.get_screenshot_as_file("C:/Users/Dell/Desktop/New folder/homepage.jpg")

