import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    @allure.step('Клик по кнопке "Конструктор"')
    def click_constructor_btn(self):
        self.find_element_located_click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_feed_btn(self):
        self.find_element_located_click(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Клик по кнопке "Войти"')
    def click_profile_area_btn(self):
        self.find_element_located_click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Переход к кнопке "Личный Кабинет" и клик на нее')
    def move_to_personal_account_btn_and_click(self):
        self.find_element_located_click(MainPageLocators.ACCOUNT_BUTTON)

    @allure.step('Проверка отображения формы конструктор')
    def check_constructor_form(self):
        return self.find_element_located(MainPageLocators.CONSTRUCTOR_FORM)

    @allure.step('Проверка отображения формы ленты заказов')
    def check_orders_feed_form(self):
        return self.find_element_located(MainPageLocators.ORDER_FEED_FORM)

    @allure.step('Клик по Флюорисцентной булке RD-D3')
    def click_fluorescent_bun_btn(self):
        self.find_element_located_click(MainPageLocators.FLU_BUN_BUTTON)

    @allure.step('Проверка отображения формы "Информации о булке"')
    def check_fluorescent_bun_form(self):
        return self.find_element_located(MainPageLocators.INGREDIENTS_POPUP_FORM)

    @allure.step('Проверка закрытия формы "Информация о булке"')
    def check_close_fluorescent_bun_form(self):
        return self.find_element_not_located(MainPageLocators.INGREDIENTS_POPUP_FORM)

    @allure.step('Закрытие формы информации об ингридиенте')
    def close_popup_form(self):
        self.find_element_located_click(MainPageLocators.CLOSE_POPUP_FORM)

    @allure.step('Добавить булку в корзину')
    def add_bun(self):
        self.drag_and_drop(MainPageLocators.FLU_BUN_BUTTON, MainPageLocators.ORDER_BASKET)

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_place_order_button(self):
        self.find_element_located_click(MainPageLocators.ORDER_BUTTON)

    @allure.step('Создание заказа')
    def create_order(self):
        self.add_bun()
        self.click_place_order_button()

    @allure.step('Получение значения счетчика ингредиента')
    def check_counter_ingredient(self):
        return self.get_text_locator(MainPageLocators.COUNTER_INGREDIENT)

    @allure.step('Проверка отображения формы Оформление заказа')
    def check_order_form(self):
        return self.find_element_located(MainPageLocators.ORDER_FORM)

    @allure.step('Получение номера оформленного заказа')
    def get_order_number(self):
        return self.get_text_locator(MainPageLocators.ORDER_NUMBER)

    @allure.step('Ожидание загрузки кнопки Оформить заказ')
    def wait_load_main_page(self):
        self.wait_for_load_element(MainPageLocators.ORDER_BUTTON)