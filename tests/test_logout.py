import pytest
from pages.login import SauceDemoLoginPage
from pages.logout import SauceDemoLogoutPage as LogoutPage
from utility.readproperties import ReadConfig
from utility.db_connection import get_users_from_db
from utility.logger import Logger

logger = Logger.setup_logger()

@pytest.mark.usefixtures("setup")
class TestLogout:

    @pytest.mark.order(3)
    @pytest.mark.parametrize("username,password", get_users_from_db(valid=True))
    def test_logout(self, setup, username, password):
        driver = setup
        url = ReadConfig().get_application_url()
        driver.get(url)
        logger.info("Opened SauceDemo URL")

        # Login first
        login_page = SauceDemoLoginPage(driver)
        login_page.login(username, password)
        logger.info(f"Logged in with user: {username}")

        # Perform logout
        logout_page = LogoutPage(driver)
        logout_page.logout()
