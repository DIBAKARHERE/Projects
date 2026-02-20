import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

file_path = "C:\\Users\\AZURE\\Downloads\\download.xlsx"
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/upload-download-test/")
driver.maximize_window()
Dict={}

# driver.find_element(By.CSS_SELECTOR, "#downloadButton").click()
file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_input.send_keys(file_path)   # to select for upload file we have to pass the file path inside send_keys

wait = WebDriverWait(driver, 5)
toast_locator = (By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)")
wait.until(expected_conditions.visibility_of_element_located(toast_locator))
print(driver.find_element(*toast_locator).text) # **** driver.find_element expects 2 arguments but toast_locator is a tuple. '*' unpacks the tuple by extracting 2 elements which is expected
# print(driver.find_element(By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)").text)

df = pd.read_excel(file_path)
print(df)
# fruit_price_dict = dict(zip(df["fruit_name"], df["price"]))  #zip fruits & prices in a dictionary
# print(fruit_price_dict)                                      #print fruit name & its price

fruit_price_list = df[["fruit_name", "price"]].to_dict("records")
#Take only the fruit name and price columns from the table, and convert each row into a dictionary
print(fruit_price_list)
