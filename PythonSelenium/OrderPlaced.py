import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
#Service("/chrome_driver_path/chromedriver.exe")
#If chrome driver is blocked by vpn download chrome driver compatible to chrome version
driver.get("https://rahulshettyacademy.com/client/auth/login")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("dibakarkanjilal@azuresys.com")
driver.find_element(By.CSS_SELECTOR, "#userPassword").send_keys("Azure@8981") #CSS_SELECTOR #ID method
driver.find_element(By.CSS_SELECTOR, ".btn-block").click()

print(driver.title)
print(driver.current_url)

card_body = driver.find_elements(By.CSS_SELECTOR, ".card-body")
time.sleep(2)

for product_name in card_body:
    name = product_name.find_element(By.CSS_SELECTOR, "h5 b").text

    if name == "IPHONE 13 PRO":
        product_name.find_element(By.CSS_SELECTOR, ".w-40").click()
        break

driver.find_element(By.XPATH, "//div/div[1]/button").click()
driver.find_element(By.XPATH, "//div/button[1]").click()
driver.find_element(By.XPATH, "//ul/li[4]/button").click()
driver.find_element(By.XPATH, "//div/div[3]/button[1]").click()

time.sleep(2)

checkboxes = driver.find_elements(By.CSS_SELECTOR, ".input.txt")
checkboxes[1].send_keys("321")

checkboxes = driver.find_elements(By.CSS_SELECTOR, ".input.txt")
checkboxes[2].send_keys("Dibakar Kanjilal")

driver.find_element(By.XPATH, "//input[@placeholder='Select Country']").send_keys("Ind")

time.sleep(2)

Countries = driver.find_elements(By.CSS_SELECTOR, "span[class = 'ng-star-inserted']")
#print(len(Countries))
for country in Countries:
    if country.text == "India":
        country.click()
        break

time.sleep(2)

Place_Order = driver.find_elements(By.XPATH, "//div/a")

for Submit in Place_Order:
    if Submit.text.strip() == "PLACE ORDER":
        Submit.click()
        break

time.sleep(2)

Status1 = driver.find_element(By.CSS_SELECTOR, ".hero-primary")
print(Status1.text)

Status2 = driver.find_element(By.CSS_SELECTOR, "label[class='ng-star-inserted']")
print(Status2.text)

Status3 = driver.find_element(By.CSS_SELECTOR, ".lead")
print(Status3.text)