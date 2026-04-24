from .base_page import BasePage
from .locators import MainPageLocators
from .pages.login_page import LoginPage

class MainPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)
        self.current_url = None

    def test_guest_can_go_to_login_page(browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # При создании объекта мы обязательно передаем ему тот же самый объект драйвера для работы с браузером,
        # а в качестве url передаем текущий адрес
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
