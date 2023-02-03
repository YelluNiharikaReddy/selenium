import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

# now scroll the window in three ways
driver.execute_script("window.scrollBy(0,1000)","")          # scroll for extent grid
time.sleep(5)


flag = driver.find_element(By.XPATH , "//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
driver.execute_script("arguments[0].scrollIntoView();" , flag)  # scroll until given element found
time.sleep(5)


driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")        # scroll till end
time.sleep(5)



