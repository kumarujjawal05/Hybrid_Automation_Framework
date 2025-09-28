from selenium.webdriver.common.by import By
from utility.logger import Logger   
from utility.commonfile import WebDriverHelper
from locators.saucedemo_locators import login_locators,logout_locators




class SauceDemoLogoutPage(WebDriverHelper):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger.setup_logger()   

    def logout(self):
        try:
            self.logger.info("Clicking on Hamburger menu button ...")
            hamburger = self.wait_for_element_to_be_clickable((By.XPATH, logout_locators["menu"]))
            hamburger.click()
        
            self.logger.info("Clicking on Logout button ...")
            logout_btn = self.wait_for_element_to_be_clickable((By.XPATH, logout_locators["logout"]))
            logout_btn.click()

            login_button = self.wait_for_element_to_be_visible((By.ID, login_locators["login_button"]))
            if login_button.is_displayed():
                self.logger.info("Logout successful. User redirected to login page.")
            else:
                self.logger.warning("Logout may have failed. Login button not visible.")

        except Exception as e:
            self.logger.error(f"An error occurred during logout: {str(e)}")
            raise AssertionError(f"Logout failed: {str(e)}")
