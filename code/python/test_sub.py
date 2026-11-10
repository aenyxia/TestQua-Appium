from selenium.webdriver.common.by import By
from conftest import tap, get_result

def test_subtraction(driver):
    """Test subtraction: 25 - 9 = 16"""
    tap(driver, (By.ID, "com.google.android.calculator:id/digit_2"))
    tap(driver, (By.ID, "com.google.android.calculator:id/digit_5"))
    tap(driver, (By.ID, "com.google.android.calculator:id/op_sub"))
    tap(driver, (By.ID, "com.google.android.calculator:id/digit_9"))
    tap(driver, (By.ID, "com.google.android.calculator:id/eq"))
    result = get_result(driver)
    assert result in ("16", "16.0")