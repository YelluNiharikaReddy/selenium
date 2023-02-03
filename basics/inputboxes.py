from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s = Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

driver.implicitly_wait(10)

inputboxes = driver.find_elements(By.CLASS_NAME,"text_field")      # use elements insted element

print(len(inputboxes))

# how to provide value into textboxes
driver.find_element(By.ID , "RESULT_TextField-1").send_keys("Yellu Niharika")

driver.find_element(By.XPATH , "//*[@id='RESULT_TextField-2']").send_keys("Reddy")
time.sleep(5)

# how to get the status of input boxes
status = driver.find_element(By.XPATH , "//*[@id='RESULT_TextField-1']").is_displayed()
print(status)

