from utility.commonfile import WebDriverHelper
from selenium.webdriver.common.by import By
from utility.db_connection import get_products_from_db


class AddToCartPage(WebDriverHelper):
    def __init__(self, driver):
        super().__init__(driver)


    def add_to_cart(self):
        try:
            click_cart_button = self.wait_for_element_to_be_clickable((By.ID, "shopping_cart_container"))
            click_cart_button.click()
        except Exception as e:
            print(e)

    
    def get_product_list(self):
        try:
            product_list = self.driver.find_elements(By.XPATH, '//div[@class="inventory_item_name"]')

            items = [el.text.strip() for el in product_list]
            print(f"Cart Items from UI: {items}")
            return items
        except Exception as e:
            print(f"Error fetching cart items: {e}")
            return []

    def verify_added_items_matches_db_data(self):
        db_data = get_products_from_db()   # Expected products from DB
        added_items = self.get_product_list()  # Actual products from UI

        print(f"DB Products: {db_data}")
        print(f"UI Cart Products: {added_items}")

        # Check missing items
        missing_items = [p for p in db_data if p not in added_items]
        assert not missing_items, f"Missing items in cart: {missing_items}"

        # Check mismatch (order-independent)
        assert sorted(db_data) == sorted(added_items), \
            f"DB and UI product lists do not match!\nDB: {db_data}\nUI: {added_items}"

        print("All DB products successfully verified in Cart!")