import allure

from urls_credits import Urls,Credits
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfileAreaPage


class TestProfileAreaPage:

    @allure.title('Проверка перехода в "Личный кабинет"')
    @allure.description('''
                        1. Открываем стенд
                        2. Логин
                        3. Клик по кнопке "Личный кабинет"
                        4. Проверяем отображение формы "Личный кабинет"
                        ''')
    def test_follow_to_profile_area_page(self, browser):
        main = MainPage(browser)
        login = LoginPage(browser)
        profile_area = ProfileAreaPage(browser)
        main.click_profile_area_btn()
        login.send_email_to_email_field(Credits.EMAIL_USER)
        login.send_password_to_password_field(Credits.PASSWORD_USER)
        login.click_login_btn()
        main.check_profile_area_btn()
        main.click_profile_area_btn()
        assert profile_area.check_profile_area_form() and profile_area.current_url() == (Urls.URL_PROFILE)

    @allure.title('Проверка перехода в "История Заказов"')
    @allure.description('''
                        1. Открываем стенд
                        2. Логин
                        3. Клик по кнопке "Личный кабинет"
                        4. Клик по кноке "История заказов"
                        5. Отображение истории заказов
                        ''')
    def test_follow_to_feed_orders(self, browser):
        main = MainPage(browser)
        login = LoginPage(browser)
        profile_area = ProfileAreaPage(browser)
        main.click_profile_area_btn()
        login.send_email_to_email_field(Credits.EMAIL_USER)
        login.send_password_to_password_field(Credits.PASSWORD_USER)
        login.click_login_btn()
        main.check_profile_area_btn()
        main.click_profile_area_btn()
        profile_area.click_history_orders_btn()
        assert profile_area.check_profile_area_form() and profile_area.current_url() == (Urls.URL_HISTORY)

    @allure.title('Проверка выхода из аккаунта"')
    @allure.description('''
                        1. Открываем стенд
                        2. Логин
                        3. Клик по кнопке "Личный кабинет"
                        4. Клик по кнопке "Выход"
                        5. Проверка выхода из аккаунта
                        ''')
    def test_exit_profile_area(self, browser):
        main = MainPage(browser)
        login = LoginPage(browser)
        profile_area = ProfileAreaPage(browser)
        main.click_profile_area_btn()
        login.send_email_to_email_field(Credits.EMAIL_USER)
        login.send_password_to_password_field(Credits.PASSWORD_USER)
        login.click_login_btn()
        main.check_profile_area_btn()
        main.click_profile_area_btn()
        profile_area.click_exit_btn()
        assert login.check_authorization_form_verification() and login.current_url() == (Urls.URL_LOGIN)