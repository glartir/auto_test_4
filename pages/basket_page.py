from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_message_basket_is_empty(self): #Сообщение о то что корзина пуста
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET) , "No message that the basket is empty"

    def should_not_be_products_in_basket(self): #В корзине нет товаров
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET),  "Basket is not empty but should be"

    def should_be_empty_basket(self): # Корзина пуста и есть сообещие о том что корзина пуста
        self.should_be_message_basket_is_empty()
        self.should_not_be_products_in_basket()



