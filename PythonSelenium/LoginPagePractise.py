import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

#Service("/chrome_driver_path/chromedriver.exe")
#If chrome driver is blocked by vpn download chrome driver compatible to chrome version

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "#username").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("learning")
driver.find_element(By.XPATH, "//div/label[1]/span").click()

#driver.find_element(By.XPATH, "//div/label[2]/span").click()
#time.sleep(3)
#driver.find_element(By.CSS_SELECTOR, "#okayBtn").click()

dropdown = Select(driver.find_element(By.XPATH, "//select[@data-style='btn-info']"))
#dropdown.select_by_visible_text("Teacher")
dropdown.select_by_value("teach")

driver.find_element(By.CSS_SELECTOR, "#terms").click()

(driver.find_element(By.CSS_SELECTOR, "#signInBtn")).click()

time.sleep(5)