from selenium.webdriver.common.by import By
from conftest import tap, get_result

def test_division(driver):
    """Test division: 20 / 4 = 5"""
    tap(driver, (By.ID, "com.google.android.calculator:id/digit_2"))
    tap(driver, (By.ID, "com.google.android.calculator:id/digit_0"))
    tap(driver, (By.ID, "com.google.android.calculator:id/op_div"))
    tap(driver, (By.ID, "com.google.android.calculator:id/digit_4"))
    tap(driver, (By.ID, "com.google.android.calculator:id/eq"))
    result = get_result(driver)
    assert result in ("5", "5.0")