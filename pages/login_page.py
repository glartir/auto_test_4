from .base_page import BasePage
#from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        #вот тут вопросик но пока работает.
        assert "login" in self.url, "Url is not correct"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self,email,password):

        self.should_be_register_form()
        email_input=self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        password_input=self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input_confirm=self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_CONFIRM)
        button=self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        email_input.send_keys(email)
        password_input.send_keys(password)
        password_input_confirm.send_keys(password)
        button.click()


