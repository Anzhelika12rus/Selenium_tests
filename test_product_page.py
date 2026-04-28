import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage


# link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
BASE_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# @pytest.mark.parametrize('link',
#                          ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                           pytest.param(
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                               marks=pytest.mark.xfail
#                           ),
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, link):
#     page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()  # открываем страницу
#     page.click_button_add_to_basket()  # кликаем кнопку "add_to_basket"
#     page.solve_quiz_and_get_code()  # запускаем alert
#     page.should_be_success_message()
#     # input("Нажми Enter, чтобы закрыть браузер...")

@pytest.mark.xfail(reason="Must fall")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, BASE_LINK)
    page.open()
    page.click_button_add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, BASE_LINK)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="Must fall")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, BASE_LINK)
    page.open()
    page.click_button_add_to_basket()
    page.should_disappear_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.xfail(reason="Must fall")
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.click_button_view_basket()
    page.should_be_basket_page()



# pytest -v --tb=line --language=en test_product_page.py
# pytest -v --tb=line --language=en test_product_page.py
#  pytest -s test_product_page.py
