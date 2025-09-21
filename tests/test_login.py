pytest_plugins = ["utility.browser_config"]

import pytest
from utility.readproperties import ReadConfig
from pages.login import OrangeHRMLoginPage


@pytest.mark.usefixtures("setup")
class TestLogin:

    
    
    def test_login_with_valid_credentials(self, setup):

        url = ReadConfig().get_application_url()
        username = ReadConfig().get_username()
        password = ReadConfig().get_password()

        driver = setup
        driver.get(url)
        lp = OrangeHRMLoginPage(driver)
        lp.login(url, username, password)
        