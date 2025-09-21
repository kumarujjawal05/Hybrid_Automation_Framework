from locators.orangehrm_locators import *
from selenium.webdriver.common.by import By
from utility.commonfile import WebDriverHelper




class OrangeHRMLoginPage(WebDriverHelper):
    def __init__(self, driver):
        super().__init__(driver)


    def login(self, url, username, password):

        try:
            self.driver.get(url)

            enter_username = self.wait_for_element_to_be_visible((By.XPATH, login_locators["username"]))
            enter_username.send_keys(username)

            enter_password = self.wait_for_element_to_be_visible((By.XPATH, login_locators["password"]))
            enter_password.send_keys(password)  

            click_login_button = self.wait_for_element_to_be_clickable((By.XPATH, login_locators["login_button"]))
            click_login_button.click()

        except Exception as e:
            raise AssertionError(f"Failed to log in: {str(e)}")
