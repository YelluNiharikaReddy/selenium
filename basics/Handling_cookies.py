from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s=Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
driver =webdriver.Chrome(service=s)
driver.get("https://www.amazon.in/")

# capturing the cookies
cookies = driver.get_cookies()

# print cookies info
print(cookies)

# count of cookies
print("num of cookie before adding",len(cookies))

#add cookie
new_cookie = {"name":"mycookie","value":"1234"}
driver.add_cookie(new_cookie)
cookies_new = driver.get_cookies()
print(cookies_new)
print("num of cookies after adding",len(cookies_new))

# delete the cookie
driver.delete_cookie("session-token")    # to delete single cookie
driver.delete_all_cookies()         # to delete all cookies
afterdeleting =driver.get_cookies()
print(len(afterdeleting))