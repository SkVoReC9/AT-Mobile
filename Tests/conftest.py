import pytest
import time, datetime
from appium import webdriver
import allure
from src.Helpers.LogoutHelper import LogoutHelper
from sys import platform
from allure_commons.types import AttachmentType


@pytest.fixture(scope="session")
def driver(request):
    with allure.step("Инициализируем сессию"):
        dc = {}
        driver = None
    if platform == "win32" or platform == "linux":
        dc['platformName'] = "Android"
        dc['platform'] = "ANDROID"
        #dc['version'] = "9.0"
        dc['browserName'] = "android"
        #dc['app'] = "/root/tmp/sample_apk/mobile.apk"
        dc['deviceName'] = "samsung_galaxy_s10_10.0" #"samsung_galaxy_s6_9.0"  #NXEDU19C13005182 Локальное устройство для отладки
        dc['automationName'] = "UiAutomator2"
    else:
        dc['platformName'] = "IOS"
        dc['appium:deviceName'] = "Iphone 13 PRO"
        dc['appium:automationName'] = "XCUITest"
        dc['appium:platformVersion'] = "15.5"
        dc['appium:udid'] = "D56A0310-EB1C-4E0B-BBA6-92476AC46729"
        dc['appium:appWaitForLaunch'] = "false"
    with allure.step("Запускаем сессию"):
        driver = webdriver.Remote("http://"+request.config.getoption("--host_appium")+":4723/wd/hub", dc) #172.10.11.153 Docker 127.0.0.1 Localhost
    driver.implicitly_wait(10)
    yield driver
    with allure.step("Завершаем сессию"):
        driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--host_appium",
        action="store", default="127.0.0.1")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)

# check if a test has failed


@pytest.fixture(scope="function", autouse=True)
def test_failed_check(request):
    yield
    # request.node is an "item" because we use the default
    # "function" scope
    if request.node.rep_setup.failed:
        print("setting up a test failed!", request.node.nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            driver = request.node.funcargs['driver']
            take_screenshot(driver, request.node.nodeid)
            print("executing test failed", request.node.nodeid)
            log = LogoutHelper(driver)
            log.log_out()

# make a screenshot with a name of the test, date and time


def take_screenshot(driver, nodeid):
    time.sleep(1)
    file_name = f'{nodeid}_{datetime.datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace("/","_").replace("::","__")
    allure.attach(driver.get_screenshot_as_png(), file_name, attachment_type=AttachmentType.PNG)