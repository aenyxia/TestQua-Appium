import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Appium Options
options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "14.0"
options.device_name = "Pixel_3"
options.automation_name = "UiAutomator2"
options.app_package = "com.google.android.calculator"
options.app_activity = "com.android.calculator2.Calculator"
options.no_reset = True

APPIUM_SERVER_URL = "http://127.0.0.1:4723/wd/hub"

@pytest.fixture(scope="session", autouse=True)
def create_reports_folder():
    """Create reports folder if it doesn't exist"""
    reports_dir = r"C:\Users\Lenovo\Desktop\TestQua31-Appium\reports"
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

@pytest.fixture(scope="module")
def driver():
    """Initialize the Appium driver for the Calculator app"""
    driver = webdriver.Remote(command_executor=APPIUM_SERVER_URL, options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

# Helper Functions
def tap(driver, locator):
    """Tap a button using its locator"""
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator)).click()

def get_result(driver):
    """Get the current result from the calculator display"""
    try:
        result = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, "com.google.android.calculator:id/result_final"))
        )
    except:
        result = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, "com.google.android.calculator:id/formula"))
        )
    return result.text.strip()