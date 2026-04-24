from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_success_message(self):
        # self.click_button_add_to_basket()
        self.product_name_in_message()
        self.product_price_in_message()

    # def should_be_button_add_to_basket(self):
    #     # проверка наличия кнопки добавления товара в корзину
    #     assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_BASKET), \
    #         "Button 'Add_to_basket' not found"

    def click_button_add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET)
        link.click()

    def product_name_in_message(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(
            *ProductPageLocators.BLOCK_MESSAGE_NAME).text, \
            "Product name not in message"

    def product_price_in_message(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == self.browser.find_element(
            *ProductPageLocators.BLOCK_MESSAGE_PRICE).text, \
            "Product price not in message"
