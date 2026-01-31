from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class UrbanRoutesPage:
    # Locators
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    call_taxi_button = (By.XPATH, "//button[text()='Call a taxi']")
    supportive_plan = (By.XPATH, "//*[text()='Supportive']")
    phone_button = (By.CLASS_NAME, 'np-text')
    phone_input = (By.ID, 'phone')
    next_button = (By.XPATH, "//button[text()='Next']")
    sms_code_input = (By.ID, 'code')
    confirm_button = (By.XPATH, "//button[text()='Confirm']")
    payment_method_button = (By.CLASS_NAME, 'pp-text')
    add_card_button = (By.CLASS_NAME, 'pp-plus')
    card_number_field = (By.ID, 'number')
    cvv_field = (By.NAME, 'code')
    link_button = (By.XPATH, "//button[text()='Link']")
    comment_field = (By.ID, 'comment')
    blanket_slider = (By.CSS_SELECTOR, '.r-type-switch input')
    ice_cream_plus = (By.XPATH, "//*[text()='Ice cream']/..//div[@class='counter-plus']")
    order_button = (By.CLASS_NAME, 'smart-button-main')
    car_search_modal = (By.CLASS_NAME, 'order-body')

    def __init__(self, driver):
        self.driver = driver

    def set_address(self, from_addr, to_addr):
        self.driver.find_element(*self.from_field).send_keys(from_addr)
        self.driver.find_element(*self.to_field).send_keys(to_addr)

    def select_supportive_plan(self):
        # Only click if not already active to avoid failures
        plan = self.driver.find_element(*self.supportive_plan)
        if "active" not in plan.get_attribute("class"):
            plan.click()

    def add_ice_creams(self):
        # Loop requirement from Task 3
        plus = self.driver.find_element(*self.ice_cream_plus)
        for _ in range(2):
            plus.click()

    def click_call_taxi(self):
        self.driver.find_element(*self.call_taxi_button).click()

    def set_phone(self, phone_number):
        self.driver.find_element(*self.phone_button).click()
        self.driver.find_element(*self.phone_input).send_keys(phone_number)
        self.driver.find_element(*self.next_button).click()

    def set_sms_code(self, code):
        self.driver.find_element(*self.sms_code_input).send_keys(code)
        self.driver.find_element(*self.confirm_button).click()

    def add_card(self, card_number, card_code):
        self.driver.find_element(*self.payment_method_button).click()
        self.driver.find_element(*self.add_card_button).click()
        self.driver.find_element(*self.card_number_field).send_keys(card_number)
        # CVV field must lose focus for 'Link' to activate
        cvv_element = self.driver.find_element(*self.cvv_field)
        cvv_element.send_keys(card_code)
        cvv_element.send_keys(Keys.TAB)
        self.driver.find_element(*self.link_button).click()
        # Close payment window
        self.driver.find_element(By.XPATH, "//div[@class='payment-picker open']//button[@class='close-button']").click()

    def set_comment(self, comment):
        self.driver.find_element(*self.comment_field).send_keys(comment)

    def toggle_blanket(self):
        self.driver.find_element(*self.blanket_slider).click()

    def click_order(self):
        self.driver.find_element(*self.order_button).click()