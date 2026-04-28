from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


# def go_to_login_page(browser):
#     login_link = browser.find_element(*MainPageLocators.LOGIN_LINK)
#     login_link.click()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.click_button_view_basket()
    page.should_be_basket_page()


# pytest -v --tb=line --language=en test_main_page.py
# #  pytest -s test_main_page.py
# pytest -v --tb=line --language=en login_page.py
