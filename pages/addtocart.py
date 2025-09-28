from utility.commonfile import WebDriverHelper
from selenium.webdriver.common.by import By
from utility.db_connection import get_products_from_db
from utility.logger import Logger  
from locators.saucedemo_locators import addtocart_locators



class AddToCartPage(WebDriverHelper):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger.setup_logger()  # Initialize logger

    def add_to_cart(self):
        try:
            click_cart_button = self.wait_for_element_to_be_clickable((By.ID, addtocart_locators["cart"]))
            click_cart_button.click()
            self.logger.info("Clicked on Cart button successfully.")
        except Exception as e:
            self.logger.error(f"Error clicking cart button: {str(e)}", exc_info=True)
            raise

    def get_product_list(self):
        try:
            product_list = self.driver.find_elements(By.XPATH, addtocart_locators["product_list"])
            items = [el.text.strip() for el in product_list]
            self.logger.info(f"Cart Items from UI: {items}")
            return items
        except Exception as e:
            self.logger.error(f"Error fetching cart items: {str(e)}", exc_info=True)
            return []

    def verify_added_items_matches_db_data(self):
        try:
            db_data = get_products_from_db()   # Expected products from DB
            added_items = self.get_product_list()  # Actual products from UI

            self.logger.info(f"DB Products: {db_data}")
            self.logger.info(f"UI Cart Products: {added_items}")

            # Check missing items
            missing_items = [p for p in db_data if p not in added_items]
            if missing_items:
                self.logger.error(f"Missing items in cart: {missing_items}")
            assert not missing_items, f"Missing items in cart: {missing_items}"

            # Check mismatch (order-independent)
            if sorted(db_data) != sorted(added_items):
                self.logger.error(f"DB and UI product lists do not match!\nDB: {db_data}\nUI: {added_items}")
            assert sorted(db_data) == sorted(added_items), \
                f"DB and UI product lists do not match!\nDB: {db_data}\nUI: {added_items}"

            self.logger.info("All DB products successfully verified in Cart!")
        except AssertionError as ae:
            self.logger.error(f" Verification failed: {str(ae)}")
            raise
        except Exception as e:
            self.logger.error(f"Error during verification: {str(e)}", exc_info=True)
            raise
