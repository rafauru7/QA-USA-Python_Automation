from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UrbanRoutesPage:
    # --- LOCATORS ---
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    call_taxi_button = (By.XPATH, "//button[text()='Call a taxi']")
    supportive_plan = (By.XPATH, "//div[contains(text(), 'Supportive')]")
    phone_field = (By.ID, 'phone')
    comment_field = (By.ID, 'comment')
    ice_cream_plus = (By.XPATH, "//div[text()='+']") # Update if your selector is different
    ice_cream_counter = (By.CLASS_NAME, 'counter-value')
    blanket_switch = (By.CLASS_NAME, 'slider')
    order_button = (By.CLASS_NAME, 'smart-button')
    driver_modal = (By.CLASS_NAME, 'order-body')

    def __init__(self, driver):
        self.driver = driver

    # --- ACTION METHODS ---
    def set_address(self, from_addr, to_addr):
        self.driver.find_element(*self.from_field).send_keys(from_addr)
        self.driver.find_element(*self.to_field).send_keys(to_addr)

    def click_call_taxi(self):
        self.driver.find_element(*self.call_taxi_button).click()

    def select_supportive_plan(self):
        self.driver.find_element(*self.supportive_plan).click()

    def fill_phone(self, phone_num):
        self.driver.find_element(*self.phone_field).send_keys(phone_num)

    def set_comment(self, comment):
        self.driver.find_element(*self.comment_field).send_keys(comment)

    def toggle_blanket(self):
        self.driver.find_element(*self.blanket_switch).click()

    def add_ice_cream(self, count):
        # THIS IS THE LOOP REQUIREMENT
        for _ in range(count):
            self.driver.find_element(*self.ice_cream_plus).click()

    def click_order(self):
        self.driver.find_element(*self.order_button).click()

    # --- GETTER METHODS (FOR ASSERTIONS IN MAIN.PY) ---
    def get_from_value(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to_value(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def get_ice_cream_count(self):
        return self.driver.find_element(*self.ice_cream_counter).text

    def is_driver_modal_visible(self):
        return self.driver.find_element(*self.driver_modal).is_displayed()