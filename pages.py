import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    # Locators
    FROM_FIELD = (By.ID, 'from')
    TO_FIELD = (By.ID, 'to')
    CALL_TAXI_BUTTON = (By.XPATH, "//button[contains(@class, 'button')]")
    SUPPORTIVE_TARIFF = (By.XPATH, "//div[contains(text(), 'Supportive')]")
    PHONE_FIELD = (By.CLASS_NAME, 'np-text')
    PHONE_INPUT = (By.ID, 'phone')
    NEXT_BUTTON = (By.XPATH, "//button[text()='Next']")
    CODE_INPUT = (By.ID, 'code')
    PAYMENT_METHOD = (By.CLASS_NAME, 'pp-text')
    ADD_CARD_BUTTON = (By.CLASS_NAME, 'pp-plus')
    CARD_NUMBER_INPUT = (By.ID, 'number')
    CARD_CODE_INPUT = (By.XPATH, "//input[@placeholder='12']")
    LINK_BUTTON = (By.XPATH, "//button[text()='Link']")
    CLOSE_BUTTON = (By.XPATH, "//button[@class='close-button']")
    COMMENT_INPUT = (By.ID, 'comment')
    BLANKET_SWITCH = (By.XPATH, "//div[contains(@class, 'switch')]")
    ICE_CREAM_PLUS = (By.CLASS_NAME, 'counter-plus')
    ICE_CREAM_COUNT = (By.CLASS_NAME, 'counter-value')
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'smart-button')]")
    ORDER_MODAL = (By.CLASS_NAME, 'order-header')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def input_from_address(self, from_address):
        element = self.wait.until(EC.element_to_be_clickable(self.FROM_FIELD))
        element.clear()
        element.send_keys(from_address)

    def input_to_address(self, to_address):
        element = self.wait.until(EC.element_to_be_clickable(self.TO_FIELD))
        element.clear()
        element.send_keys(to_address)

    def get_from_address(self):
        element = self.wait.until(EC.presence_of_element_located(self.FROM_FIELD))
        return element.get_attribute('value')

    def get_to_address(self):
        element = self.wait.until(EC.presence_of_element_located(self.TO_FIELD))
        return element.get_attribute('value')

    def click_call_taxi_button(self):
        element = self.wait.until(EC.element_to_be_clickable(self.CALL_TAXI_BUTTON))
        element.click()

    def select_supportive_tariff(self):
        element = self.wait.until(EC.element_to_be_clickable(self.SUPPORTIVE_TARIFF))
        element.click()

    def is_supportive_selected(self):
        try:
            element = self.driver.find_element(By.XPATH, "//div[contains(@class, 'tcard active')]")
            return "Supportive" in element.text
        except:
            return False

    def fill_phone_number(self, phone_number):
        element = self.wait.until(EC.element_to_be_clickable(self.PHONE_FIELD))
        element.click()

        phone_input = self.wait.until(EC.element_to_be_clickable(self.PHONE_INPUT))
        phone_input.clear()
        phone_input.send_keys(phone_number)

        next_button = self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON))
        next_button.click()

    def get_phone_number(self):
        element = self.wait.until(EC.presence_of_element_located(self.PHONE_FIELD))
        return element.text

    def fill_sms_code(self, code):
        element = self.wait.until(EC.element_to_be_clickable(self.CODE_INPUT))
        element.clear()
        element.send_keys(code)

        next_button = self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON))
        next_button.click()

    def click_payment_method(self):
        element = self.wait.until(EC.element_to_be_clickable(self.PAYMENT_METHOD))
        element.click()

    def click_add_card(self):
        element = self.wait.until(EC.element_to_be_clickable(self.ADD_CARD_BUTTON))
        element.click()

    def fill_card_number(self, card_number):
        element = self.wait.until(EC.element_to_be_clickable(self.CARD_NUMBER_INPUT))
        element.clear()
        element.send_keys(card_number)

    def fill_card_code(self, card_code):
        element = self.wait.until(EC.element_to_be_clickable(self.CARD_CODE_INPUT))
        element.clear()
        element.send_keys(card_code)

    def press_tab_on_card_code(self):
        element = self.wait.until(EC.element_to_be_clickable(self.CARD_CODE_INPUT))
        element.send_keys(Keys.TAB)

    def click_link_button(self):
        element = self.wait.until(EC.element_to_be_clickable(self.LINK_BUTTON))
        element.click()

    def close_card_modal(self):
        element = self.wait.until(EC.element_to_be_clickable(self.CLOSE_BUTTON))
        element.click()

    def get_payment_method_text(self):
        element = self.wait.until(EC.presence_of_element_located(self.PAYMENT_METHOD))
        return element.text

    def fill_comment_for_driver(self, comment):
        element = self.wait.until(EC.element_to_be_clickable(self.COMMENT_INPUT))
        element.clear()
        element.send_keys(comment)

    def get_comment_for_driver(self):
        element = self.wait.until(EC.presence_of_element_located(self.COMMENT_INPUT))
        return element.get_attribute('value')

    def click_blanket_and_handkerchiefs(self):
        element = self.wait.until(EC.element_to_be_clickable(self.BLANKET_SWITCH))
        element.click()

    def is_blanket_and_handkerchiefs_selected(self):
        element = self.wait.until(EC.presence_of_element_located(self.BLANKET_SWITCH))
        return "on" in element.get_attribute('class')

    def order_ice_cream(self, count):
        element = self.wait.until(EC.element_to_be_clickable(self.ICE_CREAM_PLUS))
        for _ in range(count):
            element.click()
            time.sleep(0.5)

    def get_ice_cream_count(self):
        element = self.wait.until(EC.presence_of_element_located(self.ICE_CREAM_COUNT))
        return int(element.text)

    def click_order_button(self):
        element = self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON))
        element.click()

    def is_order_modal_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.ORDER_MODAL))
            return True
        except:
            return False