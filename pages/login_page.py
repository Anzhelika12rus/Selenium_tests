from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        # общий метод — объединяет все проверки страницы логина
        # вызывается, если нужно проверить всё сразу
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка, что текущий URL содержит "login"
        # self.browser.current_url — это текущий адрес страницы
        assert "login" in self.browser.current_url, \
            "login отсутствует в url"

    def should_be_login_form(self):
        # проверка наличия формы логина

        # проверяем поле ввода username
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), \
            "Login username input is not presented"

        # проверяем поле ввода password
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), \
            "Login password input is not presented"

    def should_be_register_form(self):
        # проверка наличия формы регистрации

        # проверяем поле email
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_USERNAME), \
            "Registration email is not presented"

        # проверяем поле password
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1), \
            "Registration password1 is not presented"

        # проверяем подтверждение пароля
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD2), \
            "Registration password2 is not presented"