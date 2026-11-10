

# ============================================================
# FILE: test_apk_inspection.py
# Optional Bonus: Tests for inspecting APK information
# ============================================================

def test_apk_package_name(driver):
    """Verify the calculator app package name"""
    current_package = driver.current_package
    assert current_package == "com.google.android.calculator"

def test_apk_activity_name(driver):
    """Verify the calculator app main activity"""
    current_activity = driver.current_activity
    assert "Calculator" in current_activity

def test_apk_version(driver):
    """Get and verify APK version information"""
    version_info = driver.execute_script("mobile: shell", {
        "command": "dumpsys",
        "args": ["package", "com.google.android.calculator"]
    })
    assert "versionName" in version_info
    assert "versionCode" in version_info

def test_apk_permissions(driver):
    """Check APK permissions"""
    permissions = driver.execute_script("mobile: shell", {
        "command": "dumpsys",
        "args": ["package", "com.google.android.calculator"]
    })
    # Calculator typically doesn't need sensitive permissions
    assert "com.google.android.calculator" in permissions

def test_apk_installation_path(driver):
    """Verify the APK installation path"""
    path_info = driver.execute_script("mobile: shell", {
        "command": "pm",
        "args": ["path", "com.google.android.calculator"]
    })
    assert "package:" in path_info
    assert ".apk" in path_info
