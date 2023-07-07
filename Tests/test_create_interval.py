import random
from src.Helpers.WellProjectHelper import WellProjectHelper
from src.Helpers.LogoutHelper import LogoutHelper
from src.Pages.LoginPage import LoginPage
from src.Pages.FieldsPage import FieldsPage
from src.Pages.WellsPage import WellsPage
from src.Pages.WellboresPage import WellborePage
from src.Pages.IntervalPage import IntervalPage

def test_create_interval(driver):
    UID = random.randint(200, 800)
    login = LoginPage(driver)
    field = FieldsPage(driver, UID)
    wells = WellsPage(driver, UID)
    wellbore = WellborePage(driver)
    interval = IntervalPage(driver)
    project_helper = WellProjectHelper(driver)
    Logout = LogoutHelper(driver)

    login.go_to_login()
    login.enter_login("admin", "admin")

    field.create_field()
    assert field.check_field() == True
    field.pick_field()
    wells.create_well()
    assert wells.check_well() == True
    wells.pick_well()
    wellbore.add_Wellbore("TestMobile")
    assert wellbore.check_wellbore()
    wellbore.Choose_Wellbore()
    project_helper.choose_construction_wellbore()
    interval.create_interval()
    assert Logout.log_out() == True
