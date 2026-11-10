import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ==================================================
# APPIUM OPTIONS
# ==================================================
options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "14.0"        # match your emulator/device version
options.device_name = "Pixel_3"          # match your AVD/device name
options.automation_name = "UiAutomator2"
options.app_package = "com.google.android.calculator"
options.app_activity = "com.android.calculator2.Calculator"
options.no_reset = True

APPIUM_SERVER_URL = "http://127.0.0.1:4723/wd/hub"

# ==================================================
# PYTEST FIXTURE
# ==================================================
@pytest.fixture(scope="module")
def driver():
    """Initialize the Appium driver for the Calculator app"""
    driver = webdriver.Remote(command_executor=APPIUM_SERVER_URL, options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

# ==================================================
# HELPER FUNCTIONS
# ==================================================
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
        # fallback if result_final does not exist
        result = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, "com.google.android.calculator:id/formula"))
        )
    return result.text.strip()

# ==================================================
# TEST CASES
# ==================================================
def test_addition(driver):
    """Test addition: 7 + 8 = 15"""
    tap(driver, (By.ID, "com.google.android.calculator:id/digit_7"))
    tap(driver, (By.ID, "com.google.android.calculator:id/op_add"))
    tap(driver, (By.ID, "com.google.android.calculator:id/digit_8"))
    tap(driver, (By.ID, "com.google.android.calculator:id/eq"))
    result = get_result(driver)
    assert result in ("15", "15.0")

def test_subtraction(driver):
    """Test subtraction: 25 - 9 = 16"""
    tap(driver, (By.ID, "com.google.android.calculator:id/digit_2"))
    tap(driver, (By.ID, "com.google.android.calculator:id/digit_5"))
    tap(driver, (By.ID, "com.google.android.calculator:id/op_sub"))
    tap(driver, (By.ID, "com.google.android.calculator:id/digit_9"))
    tap(driver, (By.ID, "com.google.android.calculator:id/eq"))
    result = get_result(driver)
    assert result in ("16", "16.0")

def test_clear_button(driver):
    """Test the clear button resets the display"""
    tap(driver, (By.ID, "com.google.android.calculator:id/digit_9"))
    tap(driver, (By.ID, "com.google.android.calculator:id/clr"))
    result = get_result(driver)
    assert result in ("", "0")

def test_multiplication(driver):
    """Test multiplication: 6 * 7 = 42"""
    tap(driver, (By.ID, "com.google.android.calculator:id/digit_6"))
    tap(driver, (By.ID, "com.google.android.calculator:id/op_mul"))
    tap(driver, (By.ID, "com.google.android.calculator:id/digit_7"))
    tap(driver, (By.ID, "com.google.android.calculator:id/eq"))
    result = get_result(driver)
    assert result in ("42", "42.0")

def test_division(driver):
    """Test division: 20 / 4 = 5"""
    tap(driver, (By.ID, "com.google.android.calculator:id/digit_2"))
    tap(driver, (By.ID, "com.google.android.calculator:id/digit_0"))
    tap(driver, (By.ID, "com.google.android.calculator:id/op_div"))
    tap(driver, (By.ID, "com.google.android.calculator:id/digit_4"))
    tap(driver, (By.ID, "com.google.android.calculator:id/eq"))
    result = get_result(driver)
    assert result in ("5", "5.0")

def test_calculator_app_installed(driver):
    """Verify that the Calculator app is installed on the device"""
    packages = driver.execute_script("mobile: shell", {
        "command": "pm",
        "args": ["list", "packages"]
    })
    assert "com.google.android.calculator" in packages