from selenium.webdriver.common.by import By
from conftest import tap, get_result

def test_clear_button(driver):
    """Test the clear button resets the display"""
    tap(driver, (By.ID, "com.google.android.calculator:id/digit_9"))
    tap(driver, (By.ID, "com.google.android.calculator:id/clr"))
    result = get_result(driver)
    assert result in ("", "0")
