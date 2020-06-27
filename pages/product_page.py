from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):


    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), " Button add_to_basket  is not presented"

    def should_be_added_to_basket(self):   # проверяем что товар добавляется в корзину, название товара в соообщение совпадает с добавленым товаром
        title=self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        title_from_alert=self.browser.find_element(*ProductPageLocators.ALERT_MESSAGE_TITLE).text

        assert title==title_from_alert , "Title from message does not match with product's title"



    def should_be_success_message(self):   # Сообщение со стоимостью корзины, совпадает с ценой товара.

        price=self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_from_alert=self.browser.find_element(*ProductPageLocators.ALERT_MESSAGE_PRICE).text

        assert price==price_from_alert , "Price of basket does not math with product's price"


    def add_product_to_basket(self):
        self.should_be_add_to_cart_button()
        button=self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()
        self.should_be_added_to_basket()
        self.should_be_success_message()





