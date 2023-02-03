import time

import openpyxl
import XLutilies
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s = Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.testyou.in/Login.aspx")
driver.maximize_window()

path = "C:/Users/Dell/Desktop/New folder/login.xlsx"
workbook = openpyxl.load_workbook(path)
rows = XLutilies.getRowcount(path,"Sheet1")
for r in range(2,6):
    user=XLutilies.readData(path,"Sheet1",r,1)
    password=XLutilies.readData(path,"Sheet1",r,2)
    driver.find_element(By.ID,"ctl00_CPHContainer_txtUserLogin").send_keys(user)
    driver.find_element(By.ID,"ctl00_CPHContainer_txtPassword").send_keys(password)
    driver.find_element(By.XPATH,"//*[@id='ctl00_CPHContainer_btnLoginn']").click()
    if driver.title=="Student Dashboard | Test Maker - TestYou":
        driver.find_element(By.ID, "ctl00_headerTopStudent_lnkbtnSignout").click()
        print("testpass")
        XLutilies.writeData(path,"Sheet1",r,3,"testpass")
    else:
        print("testfailed")
        XLutilies.writeData(path, "Sheet1", r, 3, "testfailed")




