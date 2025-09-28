import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from utility.commonfile import WebDriverHelper
from utility.db_connection import get_products_from_db
from locators.saucedemo_locators import inventory_locators

class SauceDemooInventoryPage(WebDriverHelper):
    def __init__(self, driver):
        super().__init__(driver)



    def inventory(self):

        try:

            db_product_list = get_products_from_db()
            print("Products from DB:", db_product_list)
            inventory_products = self.driver.find_elements(By.XPATH, inventory_locators["inventory_items"])
            for el in inventory_products:
                product_name = el.text.strip()
                print(f"UI Product: {product_name}")


                # Check if product is in DB list
                if product_name in db_product_list:
                    print(f"Found product in DB: {product_name}")
                    wait = WebDriverWait(self.driver, 15)
                    click_add_to_cart = self.wait_for_element_to_be_clickable((By.XPATH, inventory_locators["add_to_cart"]))
                    time.sleep(4)
                    click_add_to_cart.click()
                
                    print(f"Added to cart: {product_name}")
            print("Finished adding all DB products to cart.")


        except Exception as e:
            raise e
