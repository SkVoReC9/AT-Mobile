import random
from src.Pages.LoginPage import LoginPage
from src.Helpers.LogoutHelper import LogoutHelper
from src.Pages.FieldsPage import FieldsPage
from src.Pages.WellsPage import WellsPage


def test_create_well(driver):
    UID = random.randint(200, 800)
    login = LoginPage(driver)
    field = FieldsPage(driver, UID)
    well = WellsPage(driver, UID)
    Logout = LogoutHelper(driver)

    login.go_to_login()
    login.enter_login("admin", "admin")
    field.create_field()
    assert field.check_field() == True
    field.pick_field()
    well.create_well()
    assert well.check_well() == True
    assert Logout.log_out() == True

