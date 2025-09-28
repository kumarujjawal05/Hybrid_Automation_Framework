from utility.commonfile import WebDriverHelper
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utility.db_connection import get_address_from_db
from utility.logger import Logger   
from locators.saucedemo_locators import checkout_locators




class CheckoutPage(WebDriverHelper):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger.setup_logger()   # Initialize logger

    def complete_checkout(self, id=1):
        try:
            first_name, last_name, zipcode = get_address_from_db(id)
            self.logger.info(f"Checkout details fetched from DB: {first_name}, {last_name}, {zipcode}")


            click_checkout = self.wait_for_element_to_be_clickable((By.ID, checkout_locators["checkout"]))
            click_checkout.click()
            self.logger.info("Clicked on Checkout button.")

            enter_first_name = self.wait_for_element_to_be_clickable((By.ID, checkout_locators["firstName"]))
            enter_first_name.send_keys(first_name)
            self.logger.info(f"Entered First Name: {first_name}")

            enter_last_name = self.wait_for_element_to_be_clickable((By.ID, checkout_locators["lastName"]))
            enter_last_name.send_keys(last_name)
            self.logger.info(f"Entered Last Name: {last_name}")

            enter_zipcode = self.wait_for_element_to_be_clickable((By.ID, checkout_locators["zipCode"]))
            enter_zipcode.send_keys(zipcode)
            self.logger.info(f"Entered Zip Code: {zipcode}")

            click_continue = self.wait_for_element_to_be_clickable((By.ID, checkout_locators["continue"]))
            click_continue.click()
            self.logger.info("Clicked on Continue button.")

            click_finish = self.wait_for_element_to_be_clickable((By.ID, checkout_locators["finish"]))
            click_finish.click()
            self.logger.info("Clicked on Finish button. Checkout process completed.")

        except Exception as e:
            self.logger.error(f"Error during checkout: {str(e)}", exc_info=True)
            raise e

    def verify_order_success(self):
        try:
            success_msg = self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, checkout_locators["message"]))
            )
            assert "Thank you" in success_msg.text
            self.logger.info("Order placed successfully and verified.")
        except AssertionError:
            self.logger.error("Order success message not found or incorrect.")
            raise
        except Exception as e:
            self.logger.error(f"Error verifying order success: {str(e)}", exc_info=True)
            raise
