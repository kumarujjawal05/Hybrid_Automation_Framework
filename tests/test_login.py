import pytest
from selenium.webdriver.common.by import By
from utility.readproperties import ReadConfig
from pages.login import SauceDemoLoginPage
from utility.db_connection import get_users_from_db
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


pytest_plugins = ["utility.browser_config"]


@pytest.mark.usefixtures("setup")
class TestLogin:


    @pytest.mark.parametrize("username,password", get_users_from_db(valid=False))
    def test_invalidLogin(self, setup, username, password):
        url = ReadConfig().get_application_url()
        driver = setup
        driver.get(url)

        lp = SauceDemoLoginPage(driver)
        lp.login(username, password)

        wait = WebDriverWait(driver, 5)
        error_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
        )
        assert error_element.is_displayed()
        pytest.fail(f"Login failed for {username}") 
        print(f"Login failed for {username}: {error_element.text}")

    @pytest.mark.order(1)
    @pytest.mark.parametrize("username,password", get_users_from_db(valid=True))
    def test_validLogin(self, setup, username, password):
        url = ReadConfig().get_application_url()
        driver = setup
        driver.get(url)

        lp = SauceDemoLoginPage(driver)
        lp.login(username, password)

        wait = WebDriverWait(driver, 5)
        wait.until(EC.url_contains("inventory"))

        assert "inventory" in driver.current_url.lower()
        print(f"Login successful for {username}")