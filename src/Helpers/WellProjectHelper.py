import allure
import appium.webdriver.common.appiumby as appiumBy

class WellProjectHelper:
    def __init__(self, driver):
        self.driver = driver

    def choose_construction_wellbore(self):
        with allure.step("Переходим в конструкцию ствола"):
            self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Construction").click()

    def choose_equipment_set(self):
        with allure.step("Переходим в компоновку ствола"):
            self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Equipment").click()