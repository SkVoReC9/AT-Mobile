import random
import time
import allure

from appium.webdriver.common.touch_action import TouchAction
import appium.webdriver.common.appiumby as appiumBy
from src.Helpers.ScrollHelper import ScrollHelper


class IntervalPage:
    def __init__(self, driver):
        self.driver = driver
        self.scroll = ScrollHelper(self.driver)
        self.actions = TouchAction(driver)

    def create_interval(self):
        with allure.step("Создаем интервал"):
            self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "CreateInterval").click()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "IntervalType").click()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Select-Для бурения под кондуктор").click()
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
            "//android.view.ViewGroup[@content-desc='PhysProps']/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.EditText[1]").send_keys(1)
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
            "//android.view.ViewGroup[@content-desc='PhysProps']/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.EditText[2]").send_keys(1)
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
            "//android.view.ViewGroup[@content-desc='IntervalBound']/android.view.ViewGroup/android.widget.EditText[2]").send_keys(750)
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
                                 "//android.view.ViewGroup[@content-desc='DolotosDiam']/android.widget.EditText").send_keys(0.259)
        self.scroll.sсroll()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "SaveInterval").click()
        time.sleep(2)
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "CloseSheet").click()

    def change_interval(self):
        with allure.step("Изменяем интервал и добавляем элемент"):
            self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Interval-Для бурения под кондуктор").click()
        self.scroll.sсroll()
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
            "//android.view.ViewGroup[@content-desc='CaseOrNotInterval']/android.view.ViewGroup/android.view.ViewGroup[2]").click()
        self.scroll.sсroll()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "PipeType").click()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Select-Кондуктор").click()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "От устья до конца интервала").click()
        self.scroll.sсroll()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Цементируется").click()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "На всю длину колонны").click()
        self.scroll.sсroll()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "ElemType").click()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Select-Байпасная система").click()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "ChooseColor").click()
        self.actions.tap(None, random.randint(290, 791), random.randint(913, 1414), 1).perform()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "SaveColor").click()
        self.scroll.sсroll()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "На всю длину колонны").click()
        self.scroll.sсroll()
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
            "//android.view.ViewGroup[@content-desc='OuterPipeDiamElem']/android.widget.EditText").send_keys(0.4)
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
            "//android.view.ViewGroup[@content-desc='MethodOfDiameter']/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup").click()
        self.scroll.sсroll()

    def add_additional_options_interval(self):
        pass



