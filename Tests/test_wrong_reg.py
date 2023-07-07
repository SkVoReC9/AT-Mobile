import allure
from src.Pages.LoginPage import LoginPage
from src.Pages.RegistrationPage import RegistrationPage


@allure.story("Проверка валидации Фронта на форме логина")
def test_wrong_reg(driver):
    with allure.step("Инициализируем класс логина в форму"):
        login = LoginPage(driver)
        registration = RegistrationPage(driver)
    #login.go_to_login()
    registration.go_to_reg()
    with allure.step("Проверяем валидацию на логин и пароль"):
        assert registration.try_reg_without_log_pass() == True
    with allure.step("Проверяем валидацию на логин"):
        assert registration.try_reg_without_log() == True
    with allure.step("Проверяем валидацию на пароль"):
        assert registration.try_reg_without_pass() == True
    with allure.step("Проверяем регистрацию"):
        assert registration.try_reg_without_confpass() == True