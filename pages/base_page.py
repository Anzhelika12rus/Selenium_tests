from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoAlertPresentException
from .locators import BasePageLocators
import math


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # абстрактный метод, который проверяет, что элемент не появляется на странице в течение заданного времени
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    # хотим проверить, что какой-то элемент исчезает, то следует воспользоваться явным ожиданием вместе с функцией until_not,
    # в зависимости от того, какой результат мы ожидаем
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert # переключает управление браузером на всплывающее окно
        x = alert.text.split(" ")[2] # Достаём число x с разбивкой split(" ")[2] — это третий элемент
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert # Пытаемся получить второй alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException: # Если второго alert нет
            print("No second alert presented")

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def click_button_view_basket(self):
        link = self.browser.find_element(*BasePageLocators.BUTTON_VIEW_BACKET)
        link.click()




