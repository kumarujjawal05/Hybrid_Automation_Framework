import time
import pytest
from selenium.webdriver.common.by import By
from utility.readproperties import ReadConfig
from pages.login import OrangeHRMLoginPage
from utility.db_connection import get_users_from_db


pytest_plugins = ["utility.browser_config"]


@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.mark.parametrize("username,password", get_users_from_db())
    def test_login_with_valid_credentials(self, setup, username, password):
        url = ReadConfig().get_application_url()
        driver = setup
        driver.get(url)

        lp = OrangeHRMLoginPage(driver)
        lp.login(username, password)
        time.sleep(3)  # Wait for page to load

        # Check if Dashboard exists (successful login)
        dashboard_elements = driver.find_elements(By.XPATH, "//h6[normalize-space()='Dashboard']")

        if dashboard_elements:
            print(f"Login successful for {username}")
            assert dashboard_elements[0].is_displayed()

        else:
            #  Check if login error message is shown
            error_elements = driver.find_element(
                By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"
            )
            if error_elements:
                print(f"Login failed as expected for {username}")
                assert error_elements.is_displayed()
                pytest.fail(f"Login failed for {username}") 
            else:
                # Neither dashboard nor error visible → unexpected
                
                pytest.fail(f"Unexpected login behavior for {username}")
