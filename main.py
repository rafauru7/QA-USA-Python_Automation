import data
import helpers
from selenium import webdriver
from pages import UrbanRoutesPage
import time


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_from_address(data.ADDRESS_FROM)
        routes_page.input_to_address(data.ADDRESS_TO)
        assert routes_page.get_from_address() == data.ADDRESS_FROM
        assert routes_page.get_to_address() == data.ADDRESS_TO

    def test_select_plan(self):
        # Add in S8 - Completed
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_from_address(data.ADDRESS_FROM)
        routes_page.input_to_address(data.ADDRESS_TO)

        # Click "Call a Taxi" button
        routes_page.click_call_taxi_button()
        time.sleep(1)

        # Select Supportive plan if not already selected
        if not routes_page.is_supportive_selected():
            routes_page.select_supportive_tariff()
            time.sleep(1)

        # Verify Supportive plan is selected
        assert routes_page.is_supportive_selected() is True

    def test_fill_phone_number(self):
        # Add in S8 - Completed
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_from_address(data.ADDRESS_FROM)
        routes_page.input_to_address(data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        time.sleep(1)

        if not routes_page.is_supportive_selected():
            routes_page.select_supportive_tariff()
            time.sleep(1)

        # Fill phone number
        routes_page.fill_phone_number(data.PHONE_NUMBER)
        time.sleep(2)

        # Get SMS code
        sms_code = helpers.retrieve_phone_code(self.driver)
        routes_page.fill_sms_code(sms_code)
        time.sleep(2)

        # Verify phone is filled
        assert data.PHONE_NUMBER in routes_page.get_phone_number()

    def test_add_credit_card(self):
        # Add in S8 - Completed
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_from_address(data.ADDRESS_FROM)
        routes_page.input_to_address(data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        time.sleep(1)

        if not routes_page.is_supportive_selected():
            routes_page.select_supportive_tariff()
            time.sleep(1)

        # Open payment method
        routes_page.click_payment_method()
        time.sleep(1)

        # Add card
        routes_page.click_add_card()
        time.sleep(1)

        # Fill card details
        routes_page.fill_card_number(data.CARD_NUMBER)
        time.sleep(0.5)
        routes_page.fill_card_code(data.CARD_CODE)
        time.sleep(0.5)

        # Press TAB to trigger validation
        routes_page.press_tab_on_card_code()
        time.sleep(1)

        # Link card
        routes_page.click_link_button()
        time.sleep(2)

        # Close modal
        routes_page.close_card_modal()
        time.sleep(1)

        # Verify card is added
        assert "Card" in routes_page.get_payment_method_text()

    def test_write_comment_for_driver(self):
        # Add in S8 - Completed
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_from_address(data.ADDRESS_FROM)
        routes_page.input_to_address(data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        time.sleep(1)

        if not routes_page.is_supportive_selected():
            routes_page.select_supportive_tariff()
            time.sleep(1)

        # Fill comment
        routes_page.fill_comment_for_driver(data.MESSAGE_FOR_DRIVER)
        time.sleep(1)

        # Verify comment
        assert routes_page.get_comment_for_driver() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8 - Completed
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_from_address(data.ADDRESS_FROM)
        routes_page.input_to_address(data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        time.sleep(1)

        if not routes_page.is_supportive_selected():
            routes_page.select_supportive_tariff()
            time.sleep(1)

        # Toggle blanket and handkerchiefs
        routes_page.click_blanket_and_handkerchiefs()
        time.sleep(1)

        # Verify it's selected
        assert routes_page.is_blanket_and_handkerchiefs_selected() is True

    def test_order_ice_cream(self):
        # Add in S8 - Completed
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_from_address(data.ADDRESS_FROM)
        routes_page.input_to_address(data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        time.sleep(1)

        if not routes_page.is_supportive_selected():
            routes_page.select_supportive_tariff()
            time.sleep(1)

        # Order 2 ice creams
        routes_page.order_ice_cream(2)
        time.sleep(1)

        # Verify count is 2
        assert routes_page.get_ice_cream_count() == 2

    def test_order_taxi_and_modal_appears(self):
        # Add in S8 - Completed
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_from_address(data.ADDRESS_FROM)
        routes_page.input_to_address(data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        time.sleep(1)

        if not routes_page.is_supportive_selected():
            routes_page.select_supportive_tariff()
            time.sleep(1)

        # Fill phone number
        routes_page.fill_phone_number(data.PHONE_NUMBER)
        time.sleep(2)
        sms_code = helpers.retrieve_phone_code(self.driver)
        routes_page.fill_sms_code(sms_code)
        time.sleep(2)

        # Add payment method
        routes_page.click_payment_method()
        time.sleep(1)
        routes_page.click_add_card()
        time.sleep(1)
        routes_page.fill_card_number(data.CARD_NUMBER)
        time.sleep(0.5)
        routes_page.fill_card_code(data.CARD_CODE)
        time.sleep(0.5)
        routes_page.press_tab_on_card_code()
        time.sleep(1)
        routes_page.click_link_button()
        time.sleep(2)
        routes_page.close_card_modal()
        time.sleep(1)

        # Fill comment
        routes_page.fill_comment_for_driver(data.MESSAGE_FOR_DRIVER)
        time.sleep(1)

        # Order blanket and handkerchiefs
        routes_page.click_blanket_and_handkerchiefs()
        time.sleep(1)

        # Order ice cream
        routes_page.order_ice_cream(2)
        time.sleep(1)

        # Click order button
        routes_page.click_order_button()
        time.sleep(3)

        # Verify modal appears
        assert routes_page.is_order_modal_visible() is True