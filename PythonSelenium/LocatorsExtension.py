import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#Service("/chrome_driver_path/chromedriver.exe")
#If chrome driver is blocked by vpn download chrome driver compatible to chrome version

driver.get("https://rahulshettyacademy.com/client/auth/login")
driver.maximize_window()

#Registration

#driver.find_element(By.XPATH, "//a[contains(text(),'Register')]").click() #Don't have an account? Register here

# driver.find_element(By.LINK_TEXT, "Register").click() #register btn
# driver.find_element(By.CSS_SELECTOR, "#firstName").send_keys("Dibakar")
# driver.find_element(By.CSS_SELECTOR, "#lastName").send_keys("Kanjilal")
# driver.find_element(By.XPATH, "//form/div[2]/div[1]/input").send_keys("dibakarkanjilal@azuresys.com")
# driver.find_element(By.XPATH, "//input[@id = 'userMobile']").send_keys("8981720370")
# driver.find_element(By.XPATH, "//div/div[1]/select").click()
# driver.find_element(By.XPATH, "//select/option[4]").click()
# driver.find_element(By.XPATH, "//div/label[2]/input").click()
# driver.find_element(By.CSS_SELECTOR, "#userPassword").send_keys("Dibakar@8981")
# driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Dibakar@8981")
# driver.find_element(By.XPATH, "//input[@formcontrolname = 'required']").click()
# driver.find_element(By.XPATH, "//input[@value = 'Register']").click()

#Forgot Password

driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("dibakarkanjilal@azuresys.com")
driver.find_element(By.CSS_SELECTOR, "#userPassword").send_keys("Azure@8981") #CSS_SELECTOR #ID method
driver.find_element(By.XPATH, "//form/div[3]/input").send_keys("Azure@8981") #XPATH Parent to Child traversing method
#driver.find_element(By.CSS_SELECTOR, "form div:nth-child(3) input").send_keys("Dibakar@8981") #CSS_SELECTOR Parent to Child traversing method
driver.find_element(By.CLASS_NAME, "btn-custom").click()
#driver.find_element(By.XPATH, "//button[text()='Save New Password']").click() #Alternate way to click Save New Password
#driver.find_element(By.XPATH, "//button[@type='submit']").click() #Another alternate way

time.sleep(5)