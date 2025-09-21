from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WebDriverHelper:


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    
    def wait_for_element_to_be_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def wait_for_element_to_be_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def click_element(self, locator):
        element = self.wait_for_element_to_be_clickable(locator)
        element.click()

    
    def enter_text(self, locator, text):
        element = self.wait_for_element_to_be_visible(locator)
        element.clear()
        element.send_keys(text)
    

    def get_element_text(self, locator):
        element = self.wait_for_element_to_be_visible(locator)
        return element.text
    


