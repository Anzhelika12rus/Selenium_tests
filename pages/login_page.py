from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, \
            "login отсутствует в url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), \
            "Login username input is not presented"

        # проверяем поле ввода password
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), \
            "Login password input is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_USERNAME), \
            "Registration email is not presented"

        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1), \
            "Registration password1 is not presented"

        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD2), \
            "Registration password2 is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_USERNAME)
        email_field.send_keys(email)
        password_field_1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        password_field_1.send_keys(password)
        password_field_2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        password_field_2.send_keys(password)
        button_register = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        button_register.click()
