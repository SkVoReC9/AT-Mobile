import time
from src.Pages.LoginPage import LoginPage
from src.Helpers.LogoutHelper import LogoutHelper


def test_login(driver):
    time.sleep(5)
    login = LoginPage(driver)
    Logout = LogoutHelper(driver)
    login.go_to_login()
    login.enter_login("admin", "admin")
    assert driver.find_element_by_accessibility_id("CreateField").is_displayed()
    assert Logout.log_out() == True


