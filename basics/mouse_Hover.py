from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver import ActionChains

s = Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.orangehrm.com/")
driver.maximize_window()

resource = driver.find_element(By.XPATH , "//*[@id='navbarSupportedContent']/ul/li[3]/a")
other_resource = driver.find_element(By.XPATH , "//*[@id='navbarSupportedContent']/ul/li[3]/div/div/div/div/ul/li[4]")
orange_hrm_Api = driver.find_element(By.XPATH , "//*[@id='navbarSupportedContent']/ul/li[3]/div/div/div/div/ul/li[4]/div/div/h6[3]/a")
actions = ActionChains(driver)

actions.move_to_element(resource).move_to_element(other_resource).move_to_element(orange_hrm_Api).click().perform()