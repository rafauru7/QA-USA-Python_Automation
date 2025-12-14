import data
import helpers

class TestUrbanRoutes:
    # Task 4: Check the Server is on
    @classmethod
    def setup_class(cls):
        # The is_url_reachable function is called from helpers.py
        # using the URL from data.py.
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            # Success message printed if the server is working.
            print("Connected to the Urban Routes server.")
        else:
            # Failure message printed if the server is not working.
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    # The 8 test functions (Task 3):

    def test_set_route(self):
        # Add in S8 # Add in S8  <-- Corrected comment
        pass
        # print("function created for set route") # Optional: uncomment for testing

    def test_select_plan(self):
        # Add in S8 # Add in S8  <-- Corrected comment
        pass
        # print("function created for select plan") # Optional: uncomment for testing

    def test_fill_phone_number(self):
        # Add in S8 # Add in S8  <-- Corrected comment
        pass
        # print("function created for fill phone number") # Optional: uncomment for testing

    def test_fill_card(self):
        # Add in S8 # Add in S8  <-- Corrected comment
        pass
        # print("function created for fill card") # Optional: uncomment for testing

    def test_comment_for_driver(self):
        # Add in S8 # Add in S8  <-- Corrected comment
        pass
        # print("function created for comment for driver") # Optional: uncomment for testing

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8 # Add in S8  <-- Corrected comment
        pass
        # print("function created for order blanket and handkerchiefs") # Optional: uncomment for testing

    # Task 5: Preparing the ice cream order
    def test_order_2_ice_creams(self):
        # Add in S8 # Add in S8  <-- Corrected comment (from Task 3 structure)
        # The loop should iterate twice (range(2)).
        for i in range(2):
            # Inside the loop, add a comment saying # Add in S8 and a pass statement.
            # Add in S8
            pass

    def test_cai_search_model_appears(self):
        # Add in S8 # Add in S8  <-- Corrected comment
        pass
        # print("function created for cai search model appears") # Optional: uncomment for testing