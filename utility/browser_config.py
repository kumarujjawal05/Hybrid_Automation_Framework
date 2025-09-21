import re
import os
import pytest
import allure
import subprocess
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService  
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def get_browser_version_windows(registry_path):
    try:
        output = subprocess.check_output(
            rf'reg query "{registry_path}" /v version', shell=True, stderr=subprocess.DEVNULL
        )
        match = re.search(r"version\s+REG_SZ\s+(\d+\.\d+\.\d+\.\d+)", output.decode())
        if match:
            return match.group(1)
        else:
            return None
    except Exception:
        return None

def get_chrome_version_windows():
    return get_browser_version_windows("HKEY_LOCAL_MACHINE/SOFTWARE/Wow6432Node/Google/Chrome/Application")

def get_edge_version_windows():
    return get_browser_version_windows("HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Edge/BLBeacon")

def get_chrome_version_mac():
    try:
        command = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome --version"
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            version_string = stdout.decode('utf-8').strip()
            version_match = re.search(r'(\d+\.\d+\.\d+\.\d+)', version_string)
            if version_match:
                return version_match.group(1)
        return None
    except FileNotFoundError:
        return None

def get_edge_version_mac():
    try:
        command = "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge --version"
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            version_string = stdout.decode('utf-8').strip()
            version_match = re.search(r'(\d+\.\d+\.\d+\.\d+)', version_string)
            if version_match:
                return version_match.group(1)
        return None
    except FileNotFoundError:
        return None

def get_chrome_version():
    if sys.platform == "win32":
        return get_chrome_version_windows()
    elif sys.platform == "darwin":
        return get_chrome_version_mac()
    return None

def get_edge_version():
    if sys.platform == "win32":
        return get_edge_version_windows()
    elif sys.platform == "darwin":
        return get_edge_version_mac()
    return None

def create_webdriver(browser, headless):
    if browser == "chrome":
        driver_path = ChromeDriverManager().install()
        service = ChromeService(executable_path=driver_path)
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Chrome(service=service, options=options)
        print("Launching Chrome Browser.........")
    elif browser == "edge":
        driver_path = EdgeChromiumDriverManager().install()
        service = EdgeService(executable_path=driver_path)
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Edge(service=service, options=options)
        print("Launching Microsoft Edge Browser.........")
    else:
        # Default to Chrome if an invalid browser is specified

        if browser == "chrome":
            driver_path = ChromeDriverManager().install()
            service = ChromeService(executable_path=driver_path)
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Chrome(service=service, options=options)
            print("Launching Chrome Browser.........")
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("--browser").lower()
    headless = request.config.getoption("--headless")
    driver = create_webdriver(browser, headless)
    request.cls.driver = driver
    yield driver
    print("Closing Browser.........")
    driver.quit()

@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser").lower()

@pytest.fixture(scope="class")
def headless(request):
    return request.config.getoption("--headless")


# Register command-line arguments for the script


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="chrome", help="Specify the browser (Chrome/Edge)")
    parser.addoption('--headless', action='store_true', default=False, help="Run tests in headless mode")



# capture screenshot on failure

def pytest_runtest_makereport(item, call):
    if call.when == 'call':

        test_instance = getattr(item, 'instance', None)
        if test_instance is not None:
            driver = getattr(test_instance, 'driver', None)
            if driver is not None:
                test_result = "passed" if call.excinfo is None else "failed"
                screenshot_dir = 'screenshots'
                if not os.path.exists(screenshot_dir):
                    os.makedirs(screenshot_dir)
                screenshot_path = os.path.join(
                    screenshot_dir, f"{item.nodeid.replace('/', '_').replace(':', '_')}_{test_result}.png"
                )

                try:
                    driver.save_screenshot(screenshot_path)
                except Exception as e:
                    print(f"Error capturing screenshot: {e}")

                if os.path.exists(screenshot_path):
                    allure.attach.file(screenshot_path, name=f"{item.name}_{test_result}", attachment_type=allure.attachment_type.PNG)

                print(f"Screenshot saved at: {screenshot_path}")

        else:
            print("Test instance or WebDriver not found.")





