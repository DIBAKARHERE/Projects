import time
from selenium.webdriver.common.by import By
from Shop import ShopPage

class LoginPage:
    def __init__(self,driver):
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.signin = (By.ID, "signInBtn")
        self.driver = driver

    def login(self):
        self.driver.find_element(*self.username_input).send_keys("rahulshettyacademy")
        self.driver.find_element(*self.password_input).send_keys("Learning@830$3mK2")
        self.driver.find_element(*self.signin).click()
        time.sleep(5)                 # wait for Shop page before locating elements (safari)
        shop_page = ShopPage(self.driver)
        return shop_page

