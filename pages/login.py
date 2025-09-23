from locators.saucedemo_locators import *
from selenium.webdriver.common.by import By
from utility.commonfile import WebDriverHelper




class SauceDemoLoginPage(WebDriverHelper):
    def __init__(self, driver):
        super().__init__(driver)


    def login(self, username, password):

        try:
            

            enter_username = self.wait_for_element_to_be_visible((By.ID, login_locators["username"]))
            enter_username.send_keys(username)

            enter_password = self.wait_for_element_to_be_visible((By.ID, login_locators["password"]))
            enter_password.send_keys(password)  

            click_login_button = self.wait_for_element_to_be_clickable((By.ID, login_locators["login_button"]))
            click_login_button.click()

        except Exception as e:
            raise AssertionError(f"Failed to log in: {str(e)}")
