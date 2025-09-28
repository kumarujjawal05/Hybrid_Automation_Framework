import pytest
from selenium.webdriver.common.by import By
from pages.addtocart import AddToCartPage
from pages.checkout import CheckoutPage
from utility.db_connection import get_users_from_db
from utility.readproperties import ReadConfig
from pages.login import SauceDemoLoginPage
from pages.inventory import SauceDemooInventoryPage


pytest_plugins = ["utility.browser_config"]
@pytest.mark.usefixtures('setup')
class TestInventory:


    @pytest.mark.order(2)
    @pytest.mark.parametrize("username,password", get_users_from_db(valid=True))
    def test_inventory(self,setup, username, password):
        url = ReadConfig().get_application_url()
        driver = setup
        driver.get(url)

        lp = SauceDemoLoginPage(driver)
        lp.login(username, password)
        ip = SauceDemooInventoryPage(driver)
        addtocart = AddToCartPage(driver)
        checkout_page = CheckoutPage(driver)
        ip.inventory()
        addtocart.add_to_cart()
        addtocart.get_product_list()
        addtocart.verify_added_items_matches_db_data()
        checkout_page.complete_checkout()
        checkout_page.verify_order_success()
        

        

