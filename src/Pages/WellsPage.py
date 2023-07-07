import allure
import time

import appium.webdriver.common.appiumby as appiumBy


class WellsPage():
    def __init__(self, driver, UID):
        self.driver = driver
        self.UID = str(UID)

    def create_well(self):
        with allure.step("Создаем скважину"):
            time.sleep(5)
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "AddWell").click()
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
            "//android.view.ViewGroup[@content-desc='WellsName']/android.view.ViewGroup[1]/android.widget.EditText").\
            send_keys("AutotestWellMobile "+self.UID)
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "WellsType").click()
        time.sleep(0.5)
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Select-Водозаборная").click()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "CreateWell").click()

    def check_well(self):
        time.sleep(0.5)
        return self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Elem-AutotestWellMobile "+self.UID).is_displayed()

    def pick_well(self):
        time.sleep(1)
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Elem-AutotestWellMobile "+self.UID).click()