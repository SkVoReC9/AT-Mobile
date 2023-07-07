import time, allure
import appium.webdriver.common.appiumby as appiumBy
from src.Helpers.ScrollHelper import ScrollHelper

class FieldsPage:
    def __init__(self, driver, UID):
        self.driver = driver
        self.scroll = ScrollHelper(driver)
        self.UID = str(UID)

    def create_field(self):
        with allure.step("Создаем Месторождение и проверяем его наличие"):
            time.sleep(5)
            self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "CreateItem").click()
        time.sleep(1)
        self.driver.find_element(appiumBy.AppiumBy.XPATH,
            '//android.view.ViewGroup[@content-desc="FieldName"]/android.widget.EditText').send_keys("Autotest-Mobile "+self.UID)
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "SaveField").click()

    def check_field(self):
        time.sleep(5)
        try:
            return self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Elem-Autotest-Mobile "+self.UID).is_displayed()
        except Exception as e:
            self.scroll.sсroll()
            return self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Elem-Autotest-Mobile "+self.UID).is_displayed()



    def pick_field(self):
        time.sleep(5)
        self.driver.find_element(appiumBy.AppiumBy.ACCESSIBILITY_ID, "Elem-Autotest-Mobile "+self.UID).click()
