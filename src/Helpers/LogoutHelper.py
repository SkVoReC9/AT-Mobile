import time
import appium.webdriver.common.appiumby as appiumBy


class LogoutHelper:
    def __init__(self, driver):
        self.driver = driver
        self.tries = 0

    def log_out(self):
        while 1 != 0:
            try:
                self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Account").click()
                time.sleep(0.5)
                self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Logout").click()
                time.sleep(2)
                return self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "GoToLogin").is_displayed()
            except Exception:
                self.driver.back()
                time.sleep(1)
                self.tries += 1
                if self.tries == 12:
                    return self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Enter").is_displayed()
