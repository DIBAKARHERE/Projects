import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
#Service("/chrome_driver_path/chromedriver.exe")
#If chrome driver is blocked by vpn download chrome driver compatible to chrome version

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "#autosuggest").send_keys("Ind")

countries = driver.find_elements(By.CSS_SELECTOR, "li[class = 'ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "Indonesia":
        country.click()
        break

#print(driver.find_element(By.ID, "autosuggest").text) #text will not be extracted for this as text is not present when load page for the first time
#print(driver.find_element(By.ID, "autosuggest").get_attribute("value")) #we follow this for dynamic text extraction by following the DOM of javascript backend
assert (driver.find_element(By.ID, "autosuggest").get_attribute("value")) == "Indonesia"