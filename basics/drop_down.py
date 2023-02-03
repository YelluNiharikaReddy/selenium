from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

s = Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://www.ivolunteer.in/volunteer-sign-up?")
element = driver.find_element(By.XPATH , "//*[@id='select-month']")
drp = Select(element)

# select by visible text
drp.select_by_visible_text("January")


# select by index
drp.select_by_index(2)


# select by value
drp.select_by_value("05")
time.sleep(5)


# count the number of options  and print them
print(len(drp.options))

# print the options
all_options = drp.options
for option in all_options:
    print(option.text)
