

#link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

# 1 открываем страницу товара
# 2 нажимаем на кнопку добавить в корзину
# 3посчитать результат
# Ожидаемый результат:
#
#     Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
#     Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
#

from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page=ProductPage(browser,link)
    page.open()

    page.add_product_to_basket()


