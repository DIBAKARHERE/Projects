import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#Service("/chrome_driver_path/chromedriver.exe")
#If chrome driver is blocked by vpn download chrome driver compatible to chrome version

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

name1 = "dibakar"
name2 = "pritam"

radio_buttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radio_buttons[2].click()
assert radio_buttons[2].is_selected()
driver.find_element(By.CSS_SELECTOR, "#checkBoxOption1").click()
driver.find_element(By.CSS_SELECTOR, "#dropdown-class-example").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "option[value='option2']").click()

driver.find_element(By.CSS_SELECTOR, ".inputs").send_keys("Ind")
time.sleep(2)

countries = driver.find_elements(By.CSS_SELECTOR, ".inputs")
time.sleep(2)

for country in countries:
    if country.is_displayed() == "India":
        country.click()
        break
time.sleep(2)

display = driver.find_element(By.CSS_SELECTOR, "#name")
assert display.is_displayed()
driver.find_element(By.CSS_SELECTOR, "#hide-textbox").click()


driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name1)
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
alert = driver.switch_to.alert #javascript popup handling
alertText = alert.text
print(alertText)
alert.accept()
assert name1 in alertText
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name2)
driver.find_element(By.CSS_SELECTOR, "#confirmbtn").click()
confirm = driver.switch_to.alert
confirmText = confirm.text
print(confirmText)
confirm.accept()  #OK
#confirm.dismiss() #Cancel
assert name2 in confirmText
time.sleep(3)




