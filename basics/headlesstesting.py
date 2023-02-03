from selenium import webdriver

def Headless_chrome():
    from selenium.webdriver.chrome.service import Service
    s=Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
    ops=webdriver.ChromeOptions()
    ops.headless=True
    driver =webdriver.Chrome(service=s,options=ops)
    return driver

def Headless_edge():
    from selenium.webdriver.edge.service import Service
    s = Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
    ops = webdriver.EdgeOptions()
    ops.headless = True
    driver = webdriver.Chrome(service=s, options=ops)
    return driver

def Headless_firefox():
    from selenium.webdriver.firefox.service import Service
    s = Service("C:\ Users\Dell\Desktop\chrome driver\chromedriver.exe")
    ops = webdriver.firefoxOptions()
    ops.headless = True
    driver = webdriver.Chrome(service=s, options=ops)
    return driver


driver = Headless_chrome()
driver.get("https://www.instagram.com/")
print(driver.title)
print(driver.current_url)