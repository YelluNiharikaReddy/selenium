from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

s = Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(5)

driver.get("https://demo.automationtesting.in/Windows.html")

driver.find_element(By.XPATH , "//*[@id='Tabbed']/a/button").click()

print(driver.current_window_handle)

handles =driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)

# if we want to close particular window
if driver.title == "Frames & windows":
    driver.close()

    # driver.close()    ## close only focused window
    # driver.quit()     ## close all windows
    # to close our wish window we have to write tha "if" condition as above

