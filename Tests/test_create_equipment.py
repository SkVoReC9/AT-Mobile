import random
from src.Helpers.WellProjectHelper import WellProjectHelper
from src.Helpers.ScrollHelper import ScrollHelper
from src.Helpers.LogoutHelper import LogoutHelper
from src.Pages.EquipmentPage import EquipmentPage
from src.Pages.LoginPage import LoginPage
from src.Pages.FieldsPage import FieldsPage
from src.Pages.WellsPage import WellsPage
from src.Pages.WellboresPage import WellborePage
from src.Pages.IntervalPage import IntervalPage

def test_create_equipment(driver):
    UID = random.randint(200, 800)
    login = LoginPage(driver)
    field = FieldsPage(driver, UID)
    wells = WellsPage(driver, UID)
    wellbore = WellborePage(driver)
    equipment = EquipmentPage(driver)
    interval = IntervalPage(driver)
    project_helper = WellProjectHelper(driver)
    scroll = ScrollHelper(driver)
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
    scroll.go_back()
    project_helper.choose_equipment_set()
    equipment.create_equipment_set()
    #equipment.create_equipment_element_doloto()
    #equipment.create_equipmemt_element_pipe()
    assert equipment.check_equipment_set() == True
    assert Logout.log_out() == True
