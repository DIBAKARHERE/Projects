from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.implicitly_wait(2)
# driver.get("https://the-internet.herokuapp.com/iframe")
driver.get("https://www.tiny.cloud/docs/tinymce/latest/basic-example/")
driver.maximize_window()

driver.switch_to.frame("basic-example_ifr") #id or iframe title name also work
driver.find_element(By.CSS_SELECTOR, "#tinymce").clear()
driver.find_element(By.CSS_SELECTOR, "#tinymce").send_keys("I am learning Selenium")
print(driver.find_element(By.CSS_SELECTOR, "#tinymce").text)
driver.quit()
