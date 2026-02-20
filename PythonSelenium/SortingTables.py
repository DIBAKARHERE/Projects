from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers/")
driver.maximize_window()

veggie_list = []
sorted_veggie_list = []

driver.find_element(By.CSS_SELECTOR, "#page-menu").click()
driver.find_element(By.XPATH, "//option[text()='10']").click()

initial_list = driver.find_elements(By.XPATH, "//tr/td[1]")

for item in initial_list:
    veggie_list.append(item.text)
print(veggie_list)

driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
driver.find_element(By.CSS_SELECTOR, "#page-menu").click()
driver.find_element(By.XPATH, "//option[text()='10']").click()

sorted_list = driver.find_elements(By.XPATH, "//tr/td[1]")

for item in sorted_list:
    sorted_veggie_list.append(item.text)
print(sorted_veggie_list)

assert veggie_list != sorted_veggie_list



