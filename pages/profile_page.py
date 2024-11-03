import allure

from locators.profile_page_locators import PersonalPageLocators
from pages.base_page import BasePage


class ProfileAreaPage(BasePage):

    @allure.step('Проверка отображения формы "Личного кабинета"')
    def check_profile_area_form(self):
        return self.find_element_located(PersonalPageLocators.PROFILE)

    @allure.step('Клик по кнопке "Профиль"')
    def click_profile_btn(self):
        self.find_element_located_click(PersonalPageLocators.PROFILE_BUTTON)

    @allure.step('Клик по кнопке "История заказов"')
    def click_history_orders_btn(self):
        self.find_element_located_click(PersonalPageLocators.HISTORY_BUTTON)

    @allure.step('Проверка отображения формы "История заказов"')
    def check_history_form(self):
        return self.find_element_located(PersonalPageLocators.HISTORY_FORM)

    @allure.step('Клик по кнопке "Выход"')
    def click_exit_btn(self):
        self.find_element_located_click(PersonalPageLocators.EXIT_BUTTON)

    @allure.step('Клик по кнопке "Отмена"')
    def click_cancel_btn(self):
        self.find_element_located_click(PersonalPageLocators.CANCEL_BUTTON)

    @allure.step('Клик по кнопке "Сохранить"')
    def click_save_btn(self):
        self.find_element_located_click(PersonalPageLocators.SAVE_BUTTON)

    @allure.step('Получение номера заказа в истории')
    def get_orders_number(self):
        return self.get_text_locator(PersonalPageLocators.NUMBER_ORDER)
