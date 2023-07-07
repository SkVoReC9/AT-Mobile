import allure, appium.webdriver.common.appiumby as appiumBy
from appium import webdriver, common

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_login(self):
        try:
            self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "GoToLogin").click()
        except Exception:
            pass

    def enter_login(self, login, password):
        with allure.step("Логинимся в приложение"):
            self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Login").send_keys(login)
            self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Password").send_keys(password)
            self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Enter").click()

    def enter_login_without_log_pass(self):
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Enter").click()
        return self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Alert").is_displayed()

    def enter_login_without_pass(self, login):
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Login").send_keys(login)
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Enter").click()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Login").clear()
        self.driver.hide_keyboard('return')
        return self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Alert").is_displayed()

    def enter_pass_without_login(self, password):
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Password").send_keys(password)
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Enter").click()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Password").clear()
        self.driver.hide_keyboard('return')
        return self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Alert").is_displayed()
