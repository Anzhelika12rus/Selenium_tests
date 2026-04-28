import time

import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

BASE_URL = "http://selenium1py.pythonanywhere.com"
BASE_LINK = f"{BASE_URL}/catalogue/coders-at-work_207/"


@pytest.mark.parametrize('link',
                         [f"{BASE_URL}/catalogue/coders-at-work_207/?promo=offer0",
                          f"{BASE_URL}/catalogue/coders-at-work_207/?promo=offer1",
                          f"{BASE_URL}/catalogue/coders-at-work_207/?promo=offer2",
                          f"{BASE_URL}/catalogue/coders-at-work_207/?promo=offer3",
                          f"{BASE_URL}/catalogue/coders-at-work_207/?promo=offer4",
                          f"{BASE_URL}/catalogue/coders-at-work_207/?promo=offer5",
                          f"{BASE_URL}/catalogue/coders-at-work_207/?promo=offer6",
                          pytest.param(
                              f"{BASE_URL}/catalogue/coders-at-work_207/?promo=offer7",
                              marks=pytest.mark.xfail
                          ),
                          f"{BASE_URL}/catalogue/coders-at-work_207/?promo=offer8",
                          f"{BASE_URL}/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.click_button_add_to_basket()  # кликаем кнопку "add_to_basket"
    page.solve_quiz_and_get_code()  # запускаем alert
    page.should_be_success_message()


@pytest.mark.xfail(reason="Must fall")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, BASE_LINK)
    page.open()
    page.click_button_add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="Must fall")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, BASE_LINK)
    page.open()
    page.click_button_add_to_basket()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, BASE_LINK)
    page.open()
    page.should_be_login_link()


@pytest.mark.xfail(reason="Must fall")
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, BASE_LINK)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, BASE_URL)
    page.open()
    page.click_button_view_basket()
    page.should_be_basket_page()


@pytest.mark.register
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = f"{BASE_URL}/en-gb/accounts/login/"
        self.page = LoginPage(browser, link)  # создаёт объект Page Object для этой страницы
        self.page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        self.page.register_new_user(email, password)
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, BASE_LINK)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, BASE_LINK)
        page.open()
        page.click_button_add_to_basket()
        page.should_be_success_message()

# pytest -m register test_product_page.py
# pytest -v --tb=line --language=en test_product_page.py
#  pytest -s test_product_page.py
# pytest -v --tb=line --language=en -m need_review
