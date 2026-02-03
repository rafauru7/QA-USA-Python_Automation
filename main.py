import data
import helpers
from selenium import webdriver
from pages import UrbanRoutesPage

class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # Set up the driver and the page object
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.page = UrbanRoutesPage(cls.driver)

    def setup_method(self):
        # Resets the page for every individual test case
        self.driver.get(data.URBAN_ROUTES_URL)

    def test_set_address(self):
        self.page.set_address(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert self.driver.find_element(*self.page.from_field).get_property('value') == data.ADDRESS_FROM
        assert self.driver.find_element(*self.page.to_field).get_property('value') == data.ADDRESS_TO

    def test_select_supportive_plan(self):
        self.page.setup_taxi_order(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.select_supportive_plan()
        assert self.page.is_supportive_plan_selected() == True

    def test_fill_phone_number(self):
        self.page.setup_taxi_order(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.select_supportive_plan()
        self.page.set_phone(data.PHONE_NUMBER)
        code = helpers.retrieve_phone_code(self.driver)
        self.page.set_sms_code(code)
        # Check that the button text now shows the phone number
        assert self.driver.find_element(*self.page.phone_button).text == data.PHONE_NUMBER

    def test_add_credit_card(self):
        self.page.setup_taxi_order(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.select_supportive_plan()
        self.page.add_credit_card(data.CARD_NUMBER, data.CARD_CODE)
        assert self.page.get_payment_method_text() == "Card"

    def test_comment_to_driver(self):
        self.page.setup_taxi_order(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.select_supportive_plan()
        self.page.set_comment(data.MESSAGE_FOR_DRIVER)
        assert self.driver.find_element(*self.page.comment_field).get_property('value') == data.MESSAGE_FOR_DRIVER

    def test_blanket_and_tissues(self):
        self.page.setup_taxi_order(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.select_supportive_plan()
        self.page.toggle_blanket()
        assert self.page.is_blanket_checked() == True

    def test_order_two_ice_creams(self):
        self.page.setup_taxi_order(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.select_supportive_plan()
        self.page.add_ice_cream(2)
        assert self.page.get_ice_cream_count() == "2"

    def test_final_order_taxi(self):
        # Full end-to-end flow to trigger the car search modal
        self.page.setup_taxi_order(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.select_supportive_plan()
        self.page.set_phone(data.PHONE_NUMBER)
        self.page.set_sms_code(helpers.retrieve_phone_code(self.driver))
        self.page.add_credit_card(data.CARD_NUMBER, data.CARD_CODE)
        self.page.set_comment(data.MESSAGE_FOR_DRIVER)
        self.page.click_order()
        # Verify the Car Search modal from your screenshot appeared
        assert self.page.is_driver_modal_visible() == True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()