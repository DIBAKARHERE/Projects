from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class checkout_confirmation:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.CSS_SELECTOR, ".btn-success")
        self.country_input = (By.CSS_SELECTOR, "#country")
        self.country_option = (By.LINK_TEXT, "India")
        self.checkbox = (By.XPATH, "//label[@for='checkbox2']")
        self.purchase_button = (By.CSS_SELECTOR, "input[value='Purchase']")
        self.success_message = (By.CSS_SELECTOR, ".alert-success")

    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def enter_delivery_address(self,country_name):
        self.driver.find_element(*self.country_input).send_keys(country_name)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.country_option)).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.purchase_button).click()

    def validate_order(self):
        SuccessText = self.driver.find_element(*self.success_message).text
        assert "Success! Thank you!" in SuccessText
        print(SuccessText)
