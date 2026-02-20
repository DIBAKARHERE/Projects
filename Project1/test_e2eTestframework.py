import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Login import LoginPage

def test_e2e(browserInstance):
    driver = browserInstance      #return driver from yield function from conftest file
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    driver.implicitly_wait(5)

    login_page = LoginPage(driver)
    shop_page = login_page.login()

    shop_page.add_product_to_cart("Nokia Edge")
    checkout_confirmation = shop_page.go_to_cart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("ind")
    checkout_confirmation.validate_order()

    # driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click() # '*' means partial text to uniquely identify
    # driver.find_element(By.LINK_TEXT, "Shop").click() # using LINK TEXT
    # driver.find_element(By.XPATH, "//a[@href='/angularpractice/shop']").click()  #using XPATH



