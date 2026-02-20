from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, ".radioButton").click()

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.CSS_SELECTOR, "#mousehover")).perform() #hover mouse cursor over an element
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).perform()
action.context_click(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()  #right click
#action.double_click(By.......).click().perform()  #double click
#action.drag_and_drop(self, source, target)