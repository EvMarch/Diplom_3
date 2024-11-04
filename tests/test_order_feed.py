import allure
import pytest

from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from pages.profile_page import ProfileAreaPage
from locators.order_page_locators import OrderFeedLocators
from locators.profile_page_locators import PersonalPageLocators
from helpers import Credits

class TestOrderFeedPage:

    @allure.title('Проверка если кликнуть на заказ, откроется всплывающее окно с деталями')
    @allure.description('''
                        1. Открываем стенд
                        2. Клик на кнопку "Лента заказов"
                        3. Клик на 1 заказ
                        4. Проверка отображения формы с деталями заказа
                        ''')
    def test_check_order_info_window(self, browser):
        main_page = MainPage(browser)
        feed_order = OrderFeedPage(browser)
        main_page.click_feed_btn()
        feed_order.click_order_info()
        assert feed_order.check_order_info_window()

    @allure.title('заказы пользователя из раздела «История заказов» отображаются на странице "Лента заказов"')
    @allure.description('''
                        1. Открываем стенд
                        2. Логин
                        3. Переход на страницу "Лента заказов"
                        4. Получаем список заказов на странице "Лента заказов"
                        5. Проверяем отображения заказа пользователя
                        ''')
    def test_check_user_orders_in_orders_history(self, browser):
        main_page = MainPage(browser)
        feed_order = OrderFeedPage(browser)
        login = LoginPage(browser)
        profile_area = ProfileAreaPage(browser)
        main_page.click_profile_area_btn()
        login.send_email_to_email_field(Credits.EMAIL_USER)
        login.send_password_to_password_field(Credits.PASSWORD_USER)
        login.click_login_btn()
        main_page.add_bun()
        main_page.click_place_order_button()
        order_id = main_page.get_order_id()
        main_page.close_popup_form()
        profile_area.click_element_if_clickable(PersonalPageLocators.BUTTON_PROFILE_PAGE)
        profile_area.click_history_orders_btn()
        order_id_history = profile_area.found_order_at_history(order_id)
        main_page.click_element_if_clickable(MainPageLocators.ORDER_FEED_BUTTON)
        order_id_order_feed = feed_order.found_order_at_feed(order_id)
        assert order_id_order_feed == order_id_history


    @allure.title('При создании нового заказа счетчик Выполнено за всё время')
    @allure.description('''
                        1. Открываем стенд
                        2. Логин
                        3. Переход на страницу "Лента заказов"
                        4. Получаем текущее значение счетчика
                        5. Проверяем увеличение счетчика
                        ''')
    def test_update_counter_orders(self, browser):
        main_page = MainPage(browser)
        feed_order = OrderFeedPage(browser)
        login = LoginPage(browser)
        main_page.click_feed_btn()
        now_counter = int(feed_order.check_counter_orders(OrderFeedLocators.TOTAL_ORDERS_COUNTER))
        main_page.click_profile_area_btn()
        login.send_email_to_email_field(Credits.EMAIL_USER)
        login.send_password_to_password_field(Credits.PASSWORD_USER)
        login.click_login_btn()
        main_page.add_bun()
        main_page.click_place_order_button()
        order_id = main_page.get_order_id()
        main_page.close_popup_form()
        main_page.click_feed_btn()
        new_counter = int(feed_order.check_counter_orders(OrderFeedLocators.TOTAL_ORDERS_COUNTER))
        assert new_counter > now_counter

    @allure.title('При создании нового заказа счетчик Выполнено за сегодня увеличивается')
    @allure.description('''
                        1. Открываем стенд
                        2. Логин
                        3. Переход на страницу "Лента заказов"
                        4. Получаем текущее значение счетчика
                        5. Проверяем увеличение счетчика
                        ''')

    def test_update_counter_orders(self, browser):
        main_page = MainPage(browser)
        feed_order = OrderFeedPage(browser)
        login = LoginPage(browser)
        main_page.click_feed_btn()
        now_counter = int(feed_order.check_counter_orders(OrderFeedLocators.TODAY_ORDERS_COUNTER))
        main_page.click_profile_area_btn()
        login.send_email_to_email_field(Credits.EMAIL_USER)
        login.send_password_to_password_field(Credits.PASSWORD_USER)
        login.click_login_btn()
        main_page.add_bun()
        main_page.click_place_order_button()
        order_id = main_page.get_order_id()
        main_page.close_popup_form()
        main_page.click_feed_btn()
        new_counter = int(feed_order.check_counter_orders(OrderFeedLocators.TODAY_ORDERS_COUNTER))
        assert new_counter > now_counter


    @allure.title('Проверка после оформления заказа его номер появляется в разделе В работе')
    @allure.description('''
                        2. Открываем стенд
                        3. Логин
                        4. Переход на страницу "Лента заказов"
                        5. Получаем заказ в списке "В работе"
                        6. Получаем список заказов пользователя
                        7. Проверяем, что заказ пользователя в списке заказов "В работе"
                        ''')
    def test_check_user_order_in_job(self, browser):
        main_page = MainPage(browser)
        feed_order = OrderFeedPage(browser)
        login = LoginPage(browser)
        main_page.click_feed_btn()
        main_page.click_profile_area_btn()
        login.send_email_to_email_field(Credits.EMAIL_USER)
        login.send_password_to_password_field(Credits.PASSWORD_USER)
        login.click_login_btn()
        main_page.add_bun()
        main_page.click_place_order_button()
        order_id = str(main_page.get_order_id())
        main_page.close_popup_form()
        main_page.click_feed_btn()
        orders_in_jobs = main_page.get_text_locator(OrderFeedLocators.ORDER_IN_JOB)

        assert order_id in orders_in_jobs
