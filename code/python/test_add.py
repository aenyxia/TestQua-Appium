from selenium.webdriver.common.by import By
from conftest import tap, get_result

def test_addition(driver):
    """Test addition: 7 + 8 = 15"""
    tap(driver, (By.ID, "com.google.android.calculator:id/digit_7"))
    tap(driver, (By.ID, "com.google.android.calculator:id/op_add"))
    tap(driver, (By.ID, "com.google.android.calculator:id/digit_8"))
    tap(driver, (By.ID, "com.google.android.calculator:id/eq"))
    result = get_result(driver)
    assert result in ("15", "15.0")
