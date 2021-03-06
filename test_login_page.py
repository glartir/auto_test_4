from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

# def test_guest_can_go_to_login_page(browser):
#     #link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()                      # открываем страницу
#     page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина

def test_guest_should_be_login_page(browser):
    #link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    # page.should_be_login_form()
    # page.should_be_register_form()