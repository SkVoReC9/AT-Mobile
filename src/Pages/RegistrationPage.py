import random
import appium.webdriver.common.appiumby as appiumBy

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_reg(self):
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID,"GoToReg").click()

    def reg_user(self):
        login = "user" + str(random.randint(1, 2000))
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "usrname").send_keys(login)
        password = "PassWo_rD"
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "pass").send_keys(password)
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "confirmpass").send_keys(password)
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Reg").click()
        self.driver.hide_keyboard('return')
        return [login, password]

    def go_back(self):
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "ReturntoLogin").click()

    def try_reg_without_log_pass(self):
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Reg").click()
        return self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID,"Alert").is_displayed()

    def try_reg_without_log(self):
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "pass").send_keys("Aaa1234545")
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Reg").click()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "pass").clear()
        self.driver.hide_keyboard('return')
        return self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Alert").is_displayed()

    def try_reg_without_pass(self):
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "usrname").send_keys("Wrong_log")
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Reg").click()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "usrname").clear()
        self.driver.hide_keyboard('return')
        return self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Alert").is_displayed()

    def try_reg_without_confpass(self):
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "usrname").send_keys("Wrong_log")
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "pass").send_keys("Aaa1234567")
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Reg").click()
        self.driver.hide_keyboard('return')
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "usrname").clear()
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "pass").clear()
        return self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Alert").is_displayed()