from selenium.webdriver.common.by import By

class OrderPageLocators:
    # локатор кнопки «Заказать» в шапке страницы
    ORDER_UP_BUTTON = [By.XPATH, ".//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']"]

    # локатор кнопки «Заказать» в середине страницы
    ORDER_DOWN_BUTTON = [By.XPATH, ".//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and text() = 'Заказать']"]

class PersonalAreaLocators:
    """Форма личного кабинета"""

    profile_form = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']")                           # Форма личного кабинета
    profile_btn = (By.XPATH, ".//a[text() = 'Профиль']")                                             # Кнопка профиль
    order_history_btn = (By.XPATH, ".//a[text() = 'История заказов']")                               # Кнопка история заказов
    history_order_form = (By.XPATH, ".//div[@class = 'Account_contentBox__2CPm3']")                  # Форма истории заказов
    number_order = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default')]")                  # Номер заказа
    cancel_btn = (By.XPATH, ".//button[text() = 'Отмена']")                                          # Кнопка отмена
    save_btn = (By.XPATH, ".//button[text() = 'Сохранить']")                                         # Кнопка сохранить
    exit_btn = (By.XPATH, ".//button[text() = 'Выход']")                                             # Кнопка выход


class OrderFeedLocators:
    """Форма Лента заказов"""

    title_orders_list = (By.XPATH, '//h1[text()="Лента заказов"]')                                   # Заголовок страницы
    orders_info = (By.XPATH, '//p[text()="Cостав"]')                                                 # Окно детали заказа
    total_orders_counter = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")  # Счетчик заказов за все время
    dayly_orders_counter = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")    # Счетчик заказов за сегодня
    number_order_in_job = (By.XPATH, ".//li[contains(@class, 'text_type_digits-default')]")          # Заказы "В работе"
    order_info_window = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem__2x95r')][1]")     # 1 заказ в истории
    order_history = (By.XPATH, './/p[contains(@class, "text_type_digits-default")]')