# credentials
# URL: https://dev.octopussaas.com/
# Username: henry@test.com
# Password: Nayan123!@

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as chromeService
from webdriver_manager.chrome import ChromeDriverManager

# prepare Chrome options and prefs before creating driver
chrome_options = Options()
# chrome_options.add_argument("--headless")

prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False,
}
chrome_options.add_experimental_option("prefs", prefs)

# use webdriver-manager to ensure a matching chromedriver is available
service_obj = chromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.get("https://dev.octopussaas.com/")
driver.delete_all_cookies()
driver.refresh()
driver.maximize_window()
driver.implicitly_wait(20)

driver.find_element(By.CSS_SELECTOR, "#login-email").send_keys("henry@test.com")
driver.find_element(By.CSS_SELECTOR, "#login-password").send_keys("Nayan123!@")
time.sleep(2)
driver.find_element(By.XPATH, "//button[text()='Log In']").click()
print(driver.title)

chrome_options = Options()

prefs = {
    "credentials_enable_service": False,  # Disable Chrome credential service
    "profile.password_manager_enabled": False,  # Disable Chrome password manager
    "profile.password_manager_leak_detection": False  # Disable password leak detection
}

chrome_options.add_experimental_option("prefs", prefs)

try:
    driver.find_element(By.XPATH, "//h6[text()='Generator Management']").click()
    driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys("cali")
    wait = WebDriverWait(driver, 30)
    hospital = wait.until(expected_conditions.visibility_of_element_located(
        (By.CSS_SELECTOR, "div[title='California Hospital Medical Center']")))
    hospital.click()
    driver.find_element(By.XPATH, "//a[text()='Generator Information']").click()
    time.sleep(5)
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
    time.sleep(5)
    wait = WebDriverWait(driver, 30)
    field1 = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[text()='34.0373967']")))

    wait = WebDriverWait(driver, 30)
    field2 = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[text()='-118.2657271']")))

    if field1.text == "34.0373967" and field2.text == "-118.2657271":
        print(f"Lat: {field1.text}, Lon: {field2.text} are valid")

    driver.find_element(By.XPATH, "//button[text()='...']").click()
    driver.find_element(By.XPATH, "//button[text()='Route Assignment']").click()
    add_service_btn = driver.find_element(By.XPATH, "//span[text()='Add a Service']")

    driver.execute_script("arguments[0].scrollIntoView(true);", add_service_btn)
    time.sleep(1)
    add_service_btn.click()

    driver.find_element(By.XPATH, "//span[text()='Add a Service']").click()

    driver.find_element(By.XPATH, "//span[text()='Route']").click()
    search_box = wait.until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder*='Search']")))
    search_box.send_keys('nay')
    route_option = wait.until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//li/div[text()='Nayan Route']")))
    route_option.click()
    print('Test is successfully completed!!')
finally:
    # driver.quit()
    pass