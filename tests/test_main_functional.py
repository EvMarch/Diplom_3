import allure

from urls_credits import Urls, Credits
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestMainPage:

    @allure.title('Проверка перехода по клику на «Конструктор»')
    @allure.description('''
                        1. Открываем стенд
                        2. Клик по кнопке "Войти в аккаунт"
                        3. Клик по кнопке "Конструктор";
                        4. Проверка отображения формы "Конструктор".
                        ''')
    def test_follow_to_constructor_page(self, browser):
        main_page = MainPage(browser)
        main_page.move_to_personal_account_btn_and_click()
        main_page.click_constructor_btn()
        assert main_page.check_constructor_form() and main_page.current_url() == Urls.URL_MAIN

    @allure.title('Проверка перехода по клику на «Лента заказов»')
    @allure.description('''
                        1. Открываем стенд
                        2. Клик по кнопке "Лента заказов";
                        3. Проверка отображения формы "Лента заказов".
                        ''')
    def test_follow_to_orders_feed_page(self, browser):
        main_page = MainPage(browser)
        main_page.click_feed_btn()
        assert main_page.check_orders_feed_form() and main_page.current_url() == Urls.URL_FEED

    @allure.title('Проверка если кликнуть на ингредиент, появится всплывающее окно с деталями')
    @allure.description('''
                        1. Открываем стенд
                        2. Клик по кнопке "Флюорисцентная булка R2-D3"
                        3. Проверка отображения высплывающего окна с деталями ингредиента
                        ''')
    def test_check_fluorescent_bun_form(self, browser):
        main_page = MainPage(browser)
        main_page.click_fluorescent_bun_btn()
        assert main_page.check_fluorescent_bun_form()

    @allure.title('Проверка всплывающее окно закрывается кликом по крестику')
    @allure.description('''
                        1. Открываем стенд
                        2. Клик по кнопке "Флюорисцентная булка R2-D3
                        3. Клик по крестику модального окна
                        4. Проверка закрытия формы "Информация об ингредиенте"
                        ''')
    def test_close_fluorescent_bun_form(self, browser):
        main_page = MainPage(browser)
        main_page.click_fluorescent_bun_btn()
        main_page.close_popup_form()
        assert main_page.check_close_fluorescent_bun_form()

    @allure.title('Проверка при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    @allure.description('''
                        1. Открываем стенд
                        2. Добавление "Флюорисцентная булка R2-D3 в корзину"
                        3. Проверка увеличения счетчика ингредиента
                        ''')
    def test_counter_ingredient(self, browser):
        main_page = MainPage(browser)
        main_page.add_bun()
        assert int(main_page.check_counter_ingredient()) > 0

    @allure.title('Проверка залогиненный пользователь может оформить заказ')
    @allure.description('''
                        1. Открываем стенд
                        2. Логин в системе;
                        3. Добавление "Флюорисцентная булка R2-D3 в корзину"
                        4. Клик по кнопке "Оформить заказ"
                        5. Проверка отображения формы заказа
                        ''')
    def test_create_order(self, browser):
        main_page = MainPage(browser)
        login = LoginPage(browser)
        main_page.click_profile_area_btn()
        login.send_email_to_email_field(Credits.EMAIL_USER)
        login.send_password_to_password_field(Credits.PASSWORD_USER)
        login.click_login_btn()
        main_page.check_profile_area_btn()
        main_page.click_profile_area_btn()
        main_page.click_constructor_btn()
        main_page.create_order()
        assert main_page.check_order_form()

