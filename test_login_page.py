from .pages.login_page import LoginPage

# Ссылка на страницу логина
link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


def test_login_page_url(browser):
    # создаём объект страницы логина (Page Object)
    page = LoginPage(browser, link)

    # открываем страницу в браузере
    page.open()

    # вызываем проверку URL
    # внутри метода будет assert, который проверяет наличие "login" в адресе
    page.should_be_login_url()


def test_login_form_is_present(browser):
    # создаём объект страницы логина
    page = LoginPage(browser, link)

    # открываем страницу
    page.open()

    # вызываем метод проверки формы логина
    # внутри проверяется наличие полей username и password
    page.should_be_login_form()


def test_register_form_is_present(browser):
    # создаём объект страницы логина
    page = LoginPage(browser, link)

    # открываем страницу
    page.open()

    # вызываем метод проверки формы регистрации
    # внутри проверяются поля email, password1, password2
    page.should_be_register_form()


# команда для запуска тестов:
# pytest test_login_page.py -v --tb=line --language=en