from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def click_add_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.BTN_BASKET)
        btn.click()

    def should_be_confirm_message(self):
        confirm_item_name = self.browser.find_element(*ProductPageLocators.CONFIRM_ITEM_NAME).text
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        assert confirm_item_name == item_name, "товар в корзине не соответствует"

    def print_price_of_basket(self):
        basket_count = self.browser.find_element(*ProductPageLocators.BASKET_COUNT).text
        confirm_basket_count = self.browser.find_element(*ProductPageLocators.CONFIRM_BASKET_COUNT).text
        assert basket_count == confirm_basket_count, "цена в корзине не соответствует"
