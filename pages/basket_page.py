from .base_page import BasePage
from .locators import BasketLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_empty_basket()
        self.should_be_text_about_empty_basket()

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketLocators.BASKET_BLOCK_INFO), \
            "Basket is not empty, but should be"

    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(*BasketLocators.MESSAGE_EMPTY_BASKET), \
            "Message 'Your basket is empty' is not presented"
