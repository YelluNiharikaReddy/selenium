import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
location=os.getcwd()

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    s = Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",{"download.default_directory" : location})
    driver =webdriver.Chrome(service=s,options=ops)
    return driver

def edge_setup():
    from selenium.webdriver.edge.service import Service
    s = Service("edge driver path paste")
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", {"download.default_directory": location})
    driver = webdriver.Chrome(service=s, options=ops)
    return driver



driver=chrome_setup()
driver.get("https://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
driver.implicitly_wait(5)
# for text file
driver.find_element(By.XPATH , "//*[@id='textbox']").send_keys("my name is niharika")     # sending the text to the file
driver.find_element(By.XPATH , "//*[@id='createTxt']").click()                            # generate file
driver.find_element(By.ID , "link-to-download").click()                     # download button
time.sleep(10)

# for pdf file
driver.find_element(By.XPATH , "//*[@id='pdfbox']").send_keys("my name is niharika")
driver.find_element(By.XPATH , "//*[@id='createPdf']").click()
driver.find_element(By.XPATH , "//*[@id='pdf-link-to-download']").click()
time.sleep(5)
driver.close()










