import random
import allure
from src.Pages.LoginPage import LoginPage
from src.Helpers.LogoutHelper import LogoutHelper

@allure.story("Проверка валидации Фронта на форме логина")
def test_wrong_login(driver):
    with allure.step("Инициализируем класс логина в форму"):
        login = LoginPage(driver)
        logout = LogoutHelper(driver)
    login.go_to_login()
    with allure.step("Проверяем валидацию на логин и пароль"):
        assert login.enter_login_without_log_pass() == True
    with allure.step("Проверяем валидацию на логин"):
        assert login.enter_pass_without_login(str(random.randint(1, 1000))) == True
    with allure.step("Проверяем валидацию на пароль"):
        assert login.enter_login_without_pass(str(random.randint(1, 1000))) == True


