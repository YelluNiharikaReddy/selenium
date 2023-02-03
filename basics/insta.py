import time

import openpyxl
import XLutilies
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import  ActionChains

s = Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.instagram.com/")
driver.maximize_window()
driver.implicitly_wait(5)
path = "C:/Users/Dell/Desktop/New folder/login.xlsx"
rows = XLutilies.getRowcount(path,"Sheet1")
cols = XLutilies.getcolumncount(path,"Sheet1")
for r in range(2,rows+1):
    user = XLutilies.readData(path,"Sheet1",r,1)
    password = XLutilies.readData(path,"Sheet1",r,2)
    driver.find_element(By.XPATH , "//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(user)
    driver.find_element(By.XPATH , "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(password)
    driver.find_element(By.XPATH ,"//*[@id='loginForm']/div/div[3]/button/div").click()
    if driver.find_element(By.CLASS_NAME,"_acan _acap _acas").is_displayed():
        print("testpass")
        XLutilies.writeData(path , "Sheet1" , r , 3 , "testpass")
    else:
        print("testfailed")
        XLutilies.writeData(path , "Sheet1" , r , 3 , "testfailed")
        time.sleep(5)
