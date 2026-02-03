from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class UrbanRoutesPage:
    # --- LOCATORS ---
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    call_taxi_button = (By.XPATH, "//button[contains(text(), 'Call a taxi')]")

    # Supportive Plan
    supportive_plan_card = (By.XPATH, "//div[@class='tcard-title' and text()='Supportive']/parent::div")
    supportive_plan_title = (By.XPATH, "//div[@class='tcard-title' and text()='Supportive']")

    # Phone Modal
    phone_button = (By.CLASS_NAME, 'np-button')
    phone_input_field = (By.ID, 'number')
    next_button = (By.XPATH, "//button[text()='Next']")
    sms_code_field = (By.ID, 'code')
    confirm_button = (By.XPATH, "//button[text()='Confirm']")

    # Payment Method
    payment_method_button = (By.CLASS_NAME, 'pp-button')
    add_card_button = (By.CLASS_NAME, 'pp-plus')
    card_number_field = (By.ID, 'number')
    card_code_field = (By.ID, 'code')  # Highlighed in your card screenshot
    link_button = (By.XPATH, "//button[text()='Link']")
    payment_method_value = (By.CLASS_NAME, 'pp-value-text')
    payment_modal_close = (By.XPATH, "//*[@class='payment-picker']//button[@class='close-button']")

    # Extras & Final Order
    comment_field = (By.ID, 'comment')
    blanket_switch = (By.CLASS_NAME, 'slider')
    blanket_checkbox = (By.CSS_SELECTOR, ".switch-input")
    ice_cream_plus = (By.XPATH, "//*[@class='counter-plus']")
    ice_cream_counter = (By.CLASS_NAME, 'counter-value')
    order_button = (By.CLASS_NAME, 'smart-button')
    driver_modal = (By.CLASS_NAME, 'order-body')

    def __init__(self, driver):
        self.driver = driver

    # --- ACTION METHODS ---
    def set_address(self, from_addr, to_addr):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.from_field))
        self.driver.find_element(*self.from_field).send_keys(from_addr)
        self.driver.find_element(*self.to_field).send_keys(to_addr)

    def setup_taxi_order(self, from_addr, to_addr):
        self.set_address(from_addr, to_addr)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.call_taxi_button))
        self.driver.find_element(*self.call_taxi_button).click()

    def select_supportive_plan(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.supportive_plan_title))
        self.driver.find_element(*self.supportive_plan_title).click()

    def set_phone(self, phone_num):
        self.driver.find_element(*self.phone_button).click()
        self.driver.find_element(*self.phone_input_field).send_keys(phone_num)
        self.driver.find_element(*self.next_button).click()

    def set_sms_code(self, code):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.sms_code_field))
        self.driver.find_element(*self.sms_code_field).send_keys(code)
        self.driver.find_element(*self.confirm_button).click()

    def add_credit_card(self, card_num, card_code):
        self.driver.find_element(*self.payment_method_button).click()
        self.driver.find_element(*self.add_card_button).click()
        self.driver.find_element(*self.card_number_field).send_keys(card_num)
        code_input = self.driver.find_element(*self.card_code_field)
        code_input.send_keys(card_code)
        code_input.send_keys(Keys.TAB)  # Triggers the Link button to enable
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

    # --- GETTER / ASSERTION METHODS ---
    def is_supportive_plan_selected(self):
        classes = self.driver.find_element(*self.supportive_plan_card).get_attribute('class')
        return 'active' in classes

    def get_payment_method_text(self):
        return self.driver.find_element(*self.payment_method_value).text

    def is_blanket_checked(self):
        return self.driver.find_element(*self.blanket_checkbox).get_property('checked')

    def get_ice_cream_count(self):
        return self.driver.find_element(*self.ice_cream_counter).text

    def is_driver_modal_visible(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.driver_modal)).is_displayed()