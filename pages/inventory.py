import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from utility.commonfile import WebDriverHelper
from utility.db_connection import get_products_from_db
from locators.saucedemo_locators import inventory_locators
from utility.logger import Logger  


class SauceDemooInventoryPage(WebDriverHelper):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger.setup_logger()   # Initialize logger

    def inventory(self):
        try:
            db_product_list = get_products_from_db()
            self.logger.info(f"Products from DB: {db_product_list}")

            inventory_products = self.driver.find_elements(By.XPATH, inventory_locators["inventory_items"])
            for el in inventory_products:
                product_name = el.text.strip()
                self.logger.info(f"UI Product found: {product_name}")

                # Check if product is in DB list
                if product_name in db_product_list:
                    self.logger.info(f"Found product in DB: {product_name}")
                    wait = WebDriverWait(self.driver, 15)
                    click_add_to_cart = self.wait_for_element_to_be_clickable((By.XPATH, inventory_locators["add_to_cart"]))
                    time.sleep(2)  # small wait before clicking
                    click_add_to_cart.click()
                    self.logger.info(f"Added to cart: {product_name}")

            self.logger.info("Finished adding all DB products to cart.")

        except Exception as e:
            self.logger.error(f"Error while adding products to cart: {str(e)}", exc_info=True)
            raise e
