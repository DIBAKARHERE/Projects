import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

#Service("/chrome_driver_path/chromedriver.exe")
#If chrome driver is blocked by vpn download chrome driver compatible to chrome version

driver.get("https://rahulshettyacademy.com/angularpractice/")
#ID, Xpath, CSSSelector, Classname, name, linkText
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.find_element(By.NAME, "name").send_keys("Dibakar Kanjilal")
#driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Dibakar Kanjilal") #CSS_SELECTOR
driver.find_element(By.NAME, "email").send_keys("dibakar94@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Qwerty@8981")
driver.find_element(By.CSS_SELECTOR, "#exampleCheck1").click() #Using CSS SELECTOR by #id method (CHECKBOX)
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1")) #static dropdown selection
dropdown.select_by_visible_text("Female")
#dropdown.select_by_index(1) #alternate way, select_by_index
#dropdown.select_by_value("value") #alternate way, select_by_value
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click() #Using CSS SELECTOR by #id but .classname method also applicable if unique (RADIO BTN)
#driver.find_element(By.ID, "inlineRadio2").click() (RADIO BTN)

#XPATH -> "//tagname[@attribute='value']" -> //input[@type='submit']
#To uniquely identify multiple elements we can do python index **Example below**
#driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("String")
#CSS_SELECTOR -> "tagname[attribute='value']" -> Alternate ways to identify CSS by "#id" & ".classname"
driver.find_element(By.XPATH, "//input[@type='submit']").click() #XPATH
message = driver.find_element(By.CLASS_NAME, "alert-dismissible").text #text will be extracted if text is present from the beginning
# when the site is loaded for the first time. For dynamic condition there is a different way.
print(message)
assert "success" in message
time.sleep(5)