import time
from selenium import webdriver

driver = webdriver.Chrome()

#Service("/chrome_driver_path/chromedriver.exe")
#If chrome driver is blocked by vpn download chrome driver compatible to chrome version

driver.get("https://youtube.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

time.sleep(5)
