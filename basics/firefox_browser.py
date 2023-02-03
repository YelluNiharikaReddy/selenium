from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time




fp = webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.NeverAsk.SaveToDisk,text/plain,application/pdf")
fp.set_preference("browser.download.manager.showwhenstaring",False)
fp.set_preference("browser.download.dir","c:\Downloadedfiles")
fp.set_preference("pdfjs.disabled",True)


s = Service("path of driver")
driver = webdriver.firefox(service=s,FirefoxProfile = fp)

driver.get("https://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
driver.implicitly_wait(5)

# for text file
driver.find_element(By.XPATH , "//*[@id='textbox']").send_keys("my name is niharika")     # sending the text to the file
driver.find_element(By.XPATH , "//*[@id='createTxt']").click()                            # generate file
driver.find_element(By.XPATH , "//*[@id='link-to-download']").click()                     # download button
time.sleep(10)

# for pdf file
driver.find_element(By.XPATH , "//*[@id='pdfbox']").send_keys("my name is niharika")
driver.find_element(By.XPATH , "//*[@id='createPdf']").click()
driver.find_element(By.XPATH , "//*[@id='pdf-link-to-download']").click()
time.sleep(10)
