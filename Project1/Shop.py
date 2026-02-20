from selenium.webdriver.common.by import By
from Product_Checkout import checkout_confirmation

class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_cards = (By.XPATH, "//div[@class='card h-100']")
        self.scroll = "window.scrollBy(0,500)"
        self.cart = (By.CSS_SELECTOR, ".btn-primary")

    def add_product_to_cart(self,product_name):
        products = self.driver.find_elements(*self.product_cards)
        self.driver.execute_script(self.scroll)

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == product_name:
                product.find_element(By.XPATH, "div/button").click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart).click()
        Checkout = checkout_confirmation(self.driver)
        return Checkout