import data
import helpers
from selenium import webdriver
from pages import UrbanRoutesPage


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # Mandatory setup for retrieving SMS code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}

        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

        # Check server reachability
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            cls.driver.get(data.URBAN_ROUTES_URL)

        cls.page = UrbanRoutesPage(cls.driver)

    def test_full_taxi_order_process(self):
        # Sequence of actions mimicking a real user
        self.page.set_address(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.click_call_taxi()
        self.page.select_supportive_plan()

        # Phone and SMS
        self.page.set_phone(data.PHONE_NUMBER)
        sms_code = helpers.retrieve_phone_code(self.driver)
        self.page.set_sms_code(sms_code)

        # Payment and Extras
        self.page.add_card(data.CARD_NUMBER, data.CARD_CODE)
        self.page.set_comment(data.DRIVER_COMMENT)
        self.page.toggle_blanket()
        self.page.add_ice_creams()

        # Final Verification
        self.page.click_order()
        assert self.driver.find_element(*self.page.car_search_modal).is_displayed()

    @classmethod
    def teardown_class(cls):
        # Clean up browser session
        cls.driver.quit()