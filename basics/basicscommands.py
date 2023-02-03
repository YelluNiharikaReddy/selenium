from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
driver.get("https://www.youtube.com/")
driver.find_element_by_xpath("//*[@id='icon']").click()
print(driver.title)
print(driver.current_url)
time.sleep(5)
driver.close()




