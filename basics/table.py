import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://www.techlistic.com/p/demo-selenium-practice.html")

rows = len(driver.find_elements(By.XPATH , "//*[@id='customers']/tbody/tr"))


cols = len(driver.find_elements(By.XPATH , "//*[@id='customers']/tbody/tr[1]/th"))

print("num of rows",rows)
print("num of cols",cols)

time.sleep(2)

print("Company"+"          "+"Contact"+",          "+"Country")

for r in range(2,rows+1):
    for c in range(1,cols+1):
        val = driver.find_element(By.XPATH , "//*[@id='customers']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text

        print(val , end="          ")
    print()

