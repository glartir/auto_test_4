from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM=(By.CSS_SELECTOR,"#login_form")

    REGISTER_FORM=(By.CSS_SELECTOR,"#register_form")

class ProductPageLocators():

    ADD_TO_BASKET_BUTTON=(By.CSS_SELECTOR,".btn-add-to-basket")
    PRODUCT_TITLE=(By.CSS_SELECTOR,".product_main > h1")
    PRODUCT_PRICE=(By.CSS_SELECTOR,".product_main > .price_color")
    ALERT_MESSAGE_TITLE=(By.CSS_SELECTOR, ".alertinner > strong")
    ALERT_MESSAGE_PRICE=(By.CSS_SELECTOR, ".alertinner > p > strong")
    SUCCESS_MESSAGE=(By.CSS_SELECTOR, ".alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")