import time
from src.Pages.LoginPage import LoginPage
from src.Pages.RegistrationPage import RegistrationPage
from src.Helpers.LogoutHelper import LogoutHelper



def test_reg(driver):
    time.sleep(5)
    login = LoginPage(driver)
    Logout = LogoutHelper(driver)
    reg = RegistrationPage(driver)
    login.go_to_login()
    reg.go_to_reg()
    test_auth = reg.reg_user()
    reg.go_back()
    login.enter_login(test_auth[0], test_auth[1])
    assert driver.find_element_by_accessibility_id("CreateField").is_displayed()
    assert Logout.log_out() == True