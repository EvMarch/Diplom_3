import allure

from urls_credits import Urls, Credits, Person
from pages.main_page import MainPage
from pages.recovery_password_page import RecoveryPage
from pages.login_page import LoginPage


class TestRecoveryPage:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @allure.description('''
                        1. Переход на страницу сервиса;
                        2. Переход на страницу личного кабинета
                        3. Клик по кнопке "Восстановить пароль"
                        ''')
    def test_follow_to_the_password_recovery_page(self, browser):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        recovery_page = RecoveryPage(browser)
        main_page.move_to_personal_account_btn_and_click()
        login_page.click_recovery_btn()
        assert recovery_page.check_recovery_form() and recovery_page.current_url() == (Urls.URL_FORGOT_PASSWORD)

    @allure.title('Проверка ввода почты и клик по кнопке "Восстановить"')
    @allure.description('''
                        1. Переход на страницу сервиса;
                        2. Переход на страницу личного кабинета
                        3. Клик по кнопке "Восстановить пароль"
                        4. Заполнение поля "Email"
                        5. Клик на кнопку "Восстановить"
                        ''')
    def test_input_password_and_click_recovery_btn(self, browser):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        recovery_page = RecoveryPage(browser)
        main_page.move_to_personal_account_btn_and_click()
        login_page.click_recovery_btn()
        recovery_page.send_email_to_email_field(Person.create_data_correct_user()["email"])
        recovery_page.click_recovery_btn()
        assert recovery_page.check_save_btn() and recovery_page.current_url() == (Urls.URL_RECOVERY_PASSWORD)

    @allure.title('Проверка клика по кнопке показать/скрыть пароль делает поле активным — подсвечивает его"')
    @allure.description('''
                        1. Переход на страницу сервиса;
                        2. Переход на страницу личного кабинета
                        3. Клик по кнопке "Восстановить пароль"
                        4. Заполнение поля "Email"
                        5. Клик на кнопку "Восстановить"
                        6. Заполнить поле "Пароль"
                        7. Клик на кнопку "Показать"
                        ''')
    def test_checking_the_backlight_of_the_password_field(self, browser):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        recovery_page = RecoveryPage(browser)
        person_data = Person().create_data_correct_user()
        main_page.move_to_personal_account_btn_and_click()
        login_page.click_recovery_btn()
        recovery_page.send_email_to_email_field(person_data.get("email"))
        recovery_page.click_recovery_btn()
        assert recovery_page.check_active_password_field(person_data.get("password"))