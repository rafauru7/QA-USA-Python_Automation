import data
import helpers
from selenium import webdriver
from pages import UrbanRoutesPage

class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.page = UrbanRoutesPage(cls.driver)

    def setup_method(self):
        self.driver.get(data.URBAN_ROUTES_URL)

    def test_set_address(self):
        self.page.set_address(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert self.page.get_from_value() == data.ADDRESS_FROM
        assert self.page.get_to_value() == data.ADDRESS_TO

    def test_select_supportive_plan(self):
        self.page.set_address(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.click_call_taxi()
        self.page.select_supportive_plan()
        assert self.page.is_supportive_plan_selected() == True

    def test_fill_phone_number(self):
        self.page.set_address(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.click_call_taxi()
        self.page.select_supportive_plan()
        self.page.fill_phone(data.PHONE_NUMBER)
        code = helpers.retrieve_phone_code(self.driver)
        self.page.set_sms_code(code)
        assert self.page.get_phone_number_value() == data.PHONE_NUMBER

    def test_add_credit_card(self):
        self.page.set_address(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.click_call_taxi()
        self.page.select_supportive_plan()
        self.page.add_card(data.CARD_NUMBER, data.CARD_CODE)
        assert self.page.is_card_added_successfully()

    def test_comment_for_driver(self):
        self.page.set_address(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.click_call_taxi()
        self.page.select_supportive_plan()
        self.page.set_comment(data.DRIVER_COMMENT)
        assert self.page.get_comment_value() == data.DRIVER_COMMENT

    def test_order_blanket_and_tissues(self):
        self.page.set_address(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.click_call_taxi()
        self.page.select_supportive_plan()
        self.page.toggle_blanket()
        assert self.page.is_blanket_enabled() == True

    def test_order_two_ice_creams(self):
        self.page.set_address(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.click_call_taxi()
        self.page.select_supportive_plan()
        self.page.add_ice_cream(2)
        assert self.page.get_ice_cream_count() == "2"

    # --- FIXED TEST 8 (Added add_card) ---
    def test_car_search_modal_appears(self):
        self.page.set_address(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.click_call_taxi()
        self.page.select_supportive_plan()
        self.page.fill_phone(data.PHONE_NUMBER)
        self.page.set_sms_code(helpers.retrieve_phone_code(self.driver))
        # CRITICAL FIX: Link card so order can be placed
        self.page.add_card(data.CARD_NUMBER, data.CARD_CODE)
        self.page.click_order()
        assert self.page.is_driver_modal_visible()

    # --- FIXED TEST 9 (Added add_card) ---
    def test_wait_for_driver_info(self):
        self.page.set_address(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.click_call_taxi()
        self.page.select_supportive_plan()
        self.page.fill_phone(data.PHONE_NUMBER)
        self.page.set_sms_code(helpers.retrieve_phone_code(self.driver))
        # CRITICAL FIX: Link card so order can be placed
        self.page.add_card(data.CARD_NUMBER, data.CARD_CODE)
        self.page.click_order()
        assert self.page.wait_for_driver_details()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()