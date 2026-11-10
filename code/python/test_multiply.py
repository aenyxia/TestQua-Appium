from selenium.webdriver.common.by import By
from conftest import tap, get_result

def test_multiplication(driver):
    """Test multiplication: 6 * 7 = 42"""
    tap(driver, (By.ID, "com.google.android.calculator:id/digit_6"))
    tap(driver, (By.ID, "com.google.android.calculator:id/op_mul"))
    tap(driver, (By.ID, "com.google.android.calculator:id/digit_7"))
    tap(driver, (By.ID, "com.google.android.calculator:id/eq"))
    result = get_result(driver)
    assert result in ("42", "42.0")

