from utility.commonfile import WebDriverHelper
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utility.db_connection import get_address_from_db

class CheckoutPage(WebDriverHelper):
    def __init__(self, driver):
        super().__init__(driver)

    
    def complete_checkout(self,id=1):

        
        try:
            first_name, last_name, zipcode = get_address_from_db(id)

            click_checkout = self.wait_for_element_to_be_clickable((By.ID, "checkout"))
            click_checkout.click()

            enter_first_name = self.wait_for_element_to_be_clickable((By.ID, "first-name"))
            enter_first_name.send_keys(first_name)

            enter_last_name = self.wait_for_element_to_be_clickable((By.ID, "last-name"))
            enter_last_name.send_keys(last_name)

            enter_zipcode = self.wait_for_element_to_be_clickable((By.ID, "postal-code"))
            enter_zipcode.send_keys(zipcode)

            click_continue = self.wait_for_element_to_be_clickable((By.ID, "continue"))
            click_continue.click()

            click_finish = self.wait_for_element_to_be_clickable((By.ID, "finish")) 
            click_finish.click()

        except Exception as e:
            raise e

    def verify_order_success(self):
        success_msg = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
        )
        assert "Thank you" in success_msg.text
        print("Order placed successfully!")