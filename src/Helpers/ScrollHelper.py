import time
import appium.webdriver.common.appiumby as appiumBy


class ScrollHelper:
    def __init__(self, driver):
        self.driver = driver


    def sсroll(self):
        time.sleep(0.5)
        self.driver.swipe(79, 2157, 79, 1600,400)
        time.sleep(1)

    def close_sheet(self):
        time.sleep(3)
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "CloseSheet").click()
        time.sleep(1)

    def go_back(self):
        time.sleep(1)
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "GoBack").click()
        time.sleep(1)