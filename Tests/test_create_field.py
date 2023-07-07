import random
from src.Pages.LoginPage import LoginPage
from src.Pages.FieldsPage import FieldsPage
from src.Helpers.LogoutHelper import LogoutHelper


def test_create_well(driver):
    UID = random.randint(200, 800)
    login = LoginPage(driver)
    field = FieldsPage(driver, UID)
    Logout = LogoutHelper(driver)


    login.go_to_login()
    login.enter_login("admin", "admin")
    field.create_field()
    assert field.check_field() == True
    assert Logout.log_out() == True