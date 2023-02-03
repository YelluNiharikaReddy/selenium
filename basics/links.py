from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.w3.org/TR/WCAG20-TECHS/G126.html")
links = driver.find_elements(By.TAG_NAME , "a")

# to print no of links present
print(len(links))

# capture the links
for link in links:
    print(link.text)

# to click the link
driver.find_element(By.LINK_TEXT , "Introduction").click()
      # or #
driver.find_element(By.PARTIAL_LINK_TEXT , "Intro").click()
