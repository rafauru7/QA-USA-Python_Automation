from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class UrbanRoutesPage:
    # --- LOCATORS ---
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    call_taxi_button = (By.XPATH, "//button[contains(text(), 'Call a taxi')]")
    supportive_plan_card = (By.XPATH, "//div[@class='tcard-title' and text()='Supportive']/parent::div")
    supportive_plan_title = (By.XPATH, "//div[@class='tcard-title' and text()='Supportive']")
    phone_button = (By.CLASS_NAME, 'np-button')
    phone_input_field = (By.ID, 'phone')
    next_button = (By.XPATH, "//button[text()='Next']")
    sms_code_field = (By.ID, 'code')
    confirm_button = (By.XPATH, "//button[text()='Confirm']")
    payment_method_button = (By.CLASS_NAME, 'pp-button')
    add_card_button = (By.CLASS_NAME, 'pp-plus')
    card_number_field = (By.ID, 'number')
    card_code_field = (By.XPATH, '//input[@class="card-input" and @id="code"]')
    link_button = (By.XPATH, "//button[text()='Link']")
    payment_method_value = (By.CLASS_NAME, 'pp-value-text')
    payment_modal_close = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')
    comment_field = (By.ID, 'comment')
    blanket_switch = (By.CLASS_NAME, 'slider')
    blanket_checkbox = (By.CSS_SELECTOR, ".switch-input")
    ice_cream_plus = (By.XPATH, "//*[@class='counter-plus']")
    ice_cream_counter = (By.CLASS_NAME, 'counter-value')
    order_button = (By.CLASS_NAME, 'smart-button')
    driver_modal = (By.CLASS_NAME, 'order-body')
    driver_details = (By.CLASS_NAME, 'order-number') # Example for driver assignment

    def __init__(self, driver):
        self.driver = driver

    # --- ACTION METHODS ---
    def set_address(self, from_addr, to_addr):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.from_field))
        self.driver.find_element(*self.from_field).send_keys(from_addr)
        self.driver.find_element(*self.to_field).send_keys(to_addr)

    def click_call_taxi(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.call_taxi_button))
        self.driver.find_element(*self.call_taxi_button).click()

    def select_supportive_plan(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.supportive_plan_title))
        self.driver.find_element(*self.supportive_plan_title).click()

    def fill_phone(self, phone_num):
        self.driver.find_element(*self.phone_button).click()
        self.driver.find_element(*self.phone_input_field).send_keys(phone_num)
        self.driver.find_element(*self.next_button).click()

    def set_sms_code(self, code):
        self.driver.find_element(*self.sms_code_field).send_keys(code)
        self.driver.find_element(*self.confirm_button).click()

    def add_card(self, card_num, card_code):
        self.driver.find_element(*self.payment_method_button).click()
        self.driver.find_element(*self.add_card_button).click()
        self.driver.find_element(*self.card_number_field).send_keys(card_num)
        code_input = self.driver.find_element(*self.card_code_field)
        code_input.send_keys(card_code)
        code_input.send_keys(Keys.TAB)
        self.driver.find_element(*self.link_button).click()
        self.driver.find_element(*self.payment_modal_close).click()

    def set_comment(self, comment):
        self.driver.find_element(*self.comment_field).send_keys(comment)

    def toggle_blanket(self):
        self.driver.find_element(*self.blanket_switch).click()

    def add_ice_cream(self, count):
        for _ in range(count):
            self.driver.find_element(*self.ice_cream_plus).click()

    def click_order(self):
        self.driver.find_element(*self.order_button).click()

    # --- MISSING METHODS REQUESTED BY REVIEWER ---
    def get_from_value(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to_value(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def is_supportive_plan_selected(self):
        return 'active' in self.driver.find_element(*self.supportive_plan_card).get_attribute('class')

    def get_phone_number_value(self):
        return self.driver.find_element(*self.phone_button).text

    def is_card_added_successfully(self):
        return self.driver.find_element(*self.payment_method_value).text == "Card"

    def get_comment_value(self):
        return self.driver.find_element(*self.comment_field).get_property('value')

    def is_blanket_enabled(self):
        return self.driver.find_element(*self.blanket_checkbox).get_property('checked')

    def get_ice_cream_count(self):
        return self.driver.find_element(*self.ice_cream_counter).text

    def is_driver_modal_visible(self):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.driver_modal)).is_displayed()

    def wait_for_driver_details(self):
        # Long wait for the search to complete and driver info to appear
        return WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(self.driver_details)).is_displayed()