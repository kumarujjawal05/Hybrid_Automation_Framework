import pytest
from selenium.webdriver.common.by import By
from utility.db_connection import get_users_from_db
from utility.readproperties import ReadConfig
from pages.login import SauceDemoLoginPage
from pages.inventory import SauceDemooInventoryPage


pytest_plugins = ["utility.browser_config"]
@pytest.mark.usefixtures('setup')
class TestInventory:

    @pytest.mark.parametrize("username,password", get_users_from_db(valid=True))
    def test_inventory(self,setup, username, password):
        url = ReadConfig().get_application_url()
        driver = setup
        driver.get(url)

        lp = SauceDemoLoginPage(driver)
        lp.login(username, password)

        # alert = driver.switch_to.alert
        # alert.accept()
        # print(alert.text)


        ip = SauceDemooInventoryPage(driver)
        ip.inventory()

        

