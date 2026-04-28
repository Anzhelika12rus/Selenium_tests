from .pages.login_page import LoginPage

# Ссылка на страницу логина
link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


def test_login_page_url(browser):
    # создаём объект страницы логина (Page Object)
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()


def test_login_form_is_present(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


def test_register_form_is_present(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()



# команда для запуска тестов:
# pytest test_login_page.py -v --tb=line --language=en