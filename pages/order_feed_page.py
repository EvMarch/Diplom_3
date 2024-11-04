import allure

from pages.base_page import BasePage
from locators.order_page_locators import OrderFeedLocators

class OrderFeedPage(BasePage):

    @allure.step('Получение кол-ва заказов')
    def check_counter_orders(self, locators):
        return self.get_text_locator(locators)

    @allure.step('Клик на 1 заказ в "Лента заказов"')
    def click_order_info(self):
        self.find_element_located_click(OrderFeedLocators.ORDER_INFO_HISTORY)

    @allure.step('Проверка видимости формы заказа')
    def check_order_info_window(self):
        return self.find_element_located(OrderFeedLocators.ORDERS_INFO)

    @allure.step('Проверка видимости заказа')
    def check_order_window(self):
        return self.find_element_located(OrderFeedLocators.ORDER_NUMBER_TEXT)

    @allure.step('Получение заказов "В работе"')
    def get_orders_in_jobs(self):
        elements = self.get_text_locator(OrderFeedLocators.ORDER_IN_JOB)
        orders_list = []
        for element in elements:
              order_number = element[1:]
              orders_list.append(order_number)
        return orders_list

    @allure.step('Получение списка всех заказов в "Лента заказов"')
    def get_text_all_orders(self):
        elements = self.get_orders_history()
        text_list = []
        for element in elements:
            text_list.append(element)
        return text_list

    @allure.step('Получение номеров заказов')
    def get_orders_history(self):
        elements = self.get_text_locator(OrderFeedLocators.ORDERS_HISTORY)
        orders_list = []
        for element in elements:
              order_number = element.text[2:]
              orders_list.append(order_number)
        return orders_list

    @allure.step('Получение номера заказа')
    def check_counter_order(self, locators):
        return self.get_text_locator(locators)

    @allure.step("Проверка нахождение идентификатора заказа в ленте")
    def found_order_at_feed(self, order_id):
        elements = self.find_until_all_elements_located(OrderFeedLocators.ORDERS_AT_FEED)

        for element in elements:
            if order_id == element.text:
                return True
        return True

