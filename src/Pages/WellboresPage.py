import time
import allure
import appium.webdriver.common.appiumby as appiumBy
from src.Helpers.ScrollHelper import ScrollHelper

class WellborePage():
    def __init__(self, driver):
        self.driver = driver
        self.scroll = ScrollHelper(driver)

    def add_Wellbore(self, nameWellbore):
        with allure.step("Создаем ствол скважины"):
            self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "AddWellBore").click()
        time.sleep(1)
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
            "//android.view.ViewGroup[@content-desc='WellboreName']/android.view.ViewGroup[1]/android.widget.EditText").send_keys(nameWellbore)
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
            "//android.view.ViewGroup[@content-desc='WellboreDepthCurrent']/android.widget.EditText").send_keys(1250)
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
            "//android.view.ViewGroup[@content-desc='WellboreAltitude']/android.widget.EditText").send_keys(1)
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
            "//android.view.ViewGroup[@content-desc='WellboreRotorHeight']/android.widget.EditText").send_keys(10)
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
             "//android.view.ViewGroup[@content-desc='WellboreMagnetic']/android.widget.EditText").send_keys(1)
        self.scroll.sсroll()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "CreateWellbore").click()

    def Choose_Wellbore(self):
        time.sleep(0.5)
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Elem-TestMobile").click()

    def check_wellbore(self):
        time.sleep(0.5)
        try:
            return self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Elem-TestMobile").is_displayed()
        except Exception as e:
            self.scroll.sсroll()
            return self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Elem-TestMobile").is_displayed()