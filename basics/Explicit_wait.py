from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service


s = Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.expedia.co.in/")

driver.maximize_window()

driver.implicitly_wait(5)

driver.find_element(By.XPATH , "//*[@id='wizardMainRegionV2']/div/div/div/div/ul/li[2]/a/span").click()     # flight button

status = driver.find_element(By.XPATH , "//*[@id='uitk-tabs-button-container']/div/li[1]/a").is_enabled()
print(status)
driver.find_element(By.XPATH , "//*[@id='wizard-flight-tab-roundtrip']/div[2]/div[1]/div/div[1]/div/div/div/div[1]/button").send_keys("HYD")    # from

driver.find_element(By.XPATH , "//*[@id='wizard-flight-tab-roundtrip']/div[2]/div[1]/div/div[2]/div/div/div/div[1]/button").send_keys("DFW")    # to

driver.find_element(By.XPATH , "//*[@id='d1-btn']").send_keys("20/12/2022")   # depature date

time.sleep(2)

driver.find_element(By.XPATH , "//*[@id='d2-btn']").send_keys("1-1-2023")     # Return date

driver.find_element(By.XPATH , "//*[@id='wizard-flight-pwa-1']/div[3]/div[2]/button").click()    # search



# explicit wait statement use to wait for particular phase

wait = WebDriverWait(driver , 10)
variable = wait.until(ec.element_to_be_clickable(By.XPATH , "//*[@id='app-layer-base']/div/main/div/div/div/div/div[1]/section[1]/div/form/div[6]/div/div/label/span"))
variable.click()
time.sleep(5)