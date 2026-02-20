import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "input[type='search']").send_keys("on")
time.sleep(2)                                                                     #sleep is used as list needs to be loaded with elements otherwise empty list will return
Vegetables = driver.find_elements(By.XPATH, "//div[@class='product']")  #list of vegetable

for item in Vegetables:
    item.find_element(By.XPATH, "//div/button[text()='ADD TO CART']").click()    #chain instead of multiple similar button click

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()  #XPATH for text attr doesn't take '@' value

price_list = driver.find_elements(By.XPATH, "//tr/td[5]/p")

actual_price = 0
for item in price_list:
    actual_price = actual_price + int(item.text)
print(f"actual price: {actual_price}")

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)

price_after_discount = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text
print(f"price after discount: {price_after_discount}")

assert actual_price != int(price_after_discount)

driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
driver.find_element(By.XPATH, "//div/select").click()
countries = driver.find_elements(By.XPATH, "//select/option")

for country in countries:
    if country.text == "India":
        country.click()
        print(f"Thanks for shopping from {country.text}")
        break

driver.find_element(By.CSS_SELECTOR, ".chkAgree").click()
driver.find_element(By.XPATH, "//button[text()='Proceed']").click()

