from locators.saucedemo_locators import *
from selenium.webdriver.common.by import By
from utility.commonfile import WebDriverHelper
from utility.logger import Logger   


class SauceDemoLoginPage(WebDriverHelper):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger.setup_logger()   # Initialize logger

    def login(self, username, password):
        try:
            self.logger.info("Attempting to log in...")

            enter_username = self.wait_for_element_to_be_visible((By.ID, login_locators["username"]))
            enter_username.send_keys(username)
            self.logger.info(f"Entered username: {username}")

            enter_password = self.wait_for_element_to_be_visible((By.ID, login_locators["password"]))
            enter_password.send_keys(password)  
            self.logger.info("Entered password")

            click_login_button = self.wait_for_element_to_be_clickable((By.ID, login_locators["login_button"]))
            click_login_button.click()
            self.logger.info("Clicked login button")


        except Exception as e:
            self.logger.error(f"Login failed with error: {str(e)}")
            raise AssertionError(f"Failed to log in: {str(e)}")
