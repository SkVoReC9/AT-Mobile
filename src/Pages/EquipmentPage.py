import time
import random
import allure

from appium.webdriver.common.touch_action import TouchAction
import appium.webdriver.common.appiumby as appiumBy
from src.Helpers.ScrollHelper import ScrollHelper


class EquipmentPage:
    def __init__(self, driver):
        self.driver = driver
        self.scroll = ScrollHelper(self.driver)
        self.actions = TouchAction(self.driver)

    def create_equipment_set(self):
        with allure.step("Создаем компоновку"):
            self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "CreateEquipment").click()
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
            "//android.view.ViewGroup[@content-desc='EquipmentName']/android.view.ViewGroup[1]/android.widget.EditText").send_keys("ATMobile")
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
            "//android.view.ViewGroup[@content-desc='EquipmentPurpose']/android.view.ViewGroup[1]/android.widget.EditText").send_keys("AutoTest")
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
            "//android.view.ViewGroup[@content-desc='IntervalEquipment']/android.view.ViewGroup/android.widget.EditText[2]").send_keys(750)
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "CreateEquipmentSet").click()
        time.sleep(4)
        self.scroll.close_sheet()

    def check_equipment_set(self):
        return self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Equipment-ATMobile").is_displayed()

    def create_equipment_element_doloto(self):
        with allure.step("Создаем долото в компоновке"):
            self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "equipElemType").click()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Select-Долото").click()
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
            "//android.view.ViewGroup[@content-desc='PhysicalParam']/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.EditText[1]").send_keys(100)
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
            "//android.view.ViewGroup[@content-desc='PhysicalParam']/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.EditText[2]").send_keys(15000)
        self.scroll.sсroll()
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
            "//android.view.ViewGroup[@content-desc='PhysicalParam']/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[6]/android.widget.TextView").click()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Select-S-135").click()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "SelectColorElement").click()
        time.sleep(1)
        self.actions.tap(None, random.randint(290, 791), random.randint(913, 1414), 1).perform()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "SaveColor").click()
        self.scroll.sсroll()
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
            "//android.view.ViewGroup[@content-desc='ElementLenght']/android.widget.EditText").send_keys(50)
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
            "//android.view.ViewGroup[@content-desc='outerDiameter']/android.widget.EditText").send_keys(0.4)
        self.scroll.sсroll()
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
            "//android.view.ViewGroup[@content-desc='SelectPopover']/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView").click()
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
            "//android.view.ViewGroup[@content-desc='InnerDiemeter']/android.widget.EditText").send_keys(0.2)
        self.scroll.sсroll()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "AddEquipment").click()

    def create_equipmemt_element_pipe(self):
        with allure.step("Добавляем трубу в компоновку"):
            self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "equipElemType").click()
        self.scroll.sсroll()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Select-СБТ – стальная бурильная труба").click()
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
            "//android.view.ViewGroup[@content-desc='PhysicalParam']/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.EditText[1]").send_keys(10)
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
            "//android.view.ViewGroup[@content-desc='PhysicalParam']/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.EditText[2]").send_keys(450000)
        self.scroll.sсroll()
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
            "//android.view.ViewGroup[@content-desc='PhysicalParam']/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[6]/android.widget.TextView").click()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Select-S-135").click()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "SelectColorElement").click()
        time.sleep(1)
        self.actions.tap(None, random.randint(290, 791), random.randint(913, 1414), 1).perform()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "SaveColor").click()
        time.sleep(0.5)
        self.scroll.sсroll()
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
            "//android.view.ViewGroup[@content-desc='ElementLenght']/android.widget.EditText").send_keys(500)
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
            "//android.view.ViewGroup[@content-desc='outerDiameter']/android.widget.EditText").send_keys(0.27)
        self.scroll.sсroll()
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
            "//android.view.ViewGroup[@content-desc='SelectPopover']/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView").click()
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
            "//android.view.ViewGroup[@content-desc='InnerDiemeter']/android.widget.EditText").send_keys(0.175)
        self.scroll.sсroll()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "AddEquipment").click()







