from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.implicitly_wait(2)
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

print(driver.find_element(By.TAG_NAME, "h3").text) #parent window
driver.find_element(By.LINK_TEXT, "Click Here").click()

WindowsOpened = driver.window_handles #list of windows opened
driver.switch_to.window(WindowsOpened[1]) #first child window
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close() #window or tab close not like chrome
driver.switch_to.window(WindowsOpened[0]) #parent window
driver.quit() #to close the firefox driver

