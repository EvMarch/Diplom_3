from selenium.webdriver.common.by import By

class OrderFeedLocators:

    # Заголовок страницы
    ORDERS_LIST = (By.XPATH, './/h1[text()="Лента заказов"]')
    # Окно детали заказа
    ORDERS_INFO = (By.XPATH, './/p[text()="Cостав"]')
    #Компонент ленты заказов
    ORDER_OBJECT = (By.XPATH, '//*[contains(@class, "OrderHistory_link")]')
    #Текст состав в окне одного заказа
    ORDER_STRUCTURE = (By.XPATH, '//*[text()="Cостав"]')
    # Заказы в ленте
    ORDERS_AT_FEED = (By.XPATH, ".//div[@class='OrderHistory_textBox__3lgbs mb-6']//p[@class='text "
                                "text_type_digits-default']")

    # Счетчик заказов за все время
    TOTAL_ORDERS_COUNTER = (By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p")
    # Счетчик заказов за сегодня
    TODAY_ORDERS_COUNTER = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p")
    # Заказы "В работе"
    ORDER_IN_JOB = (By.XPATH, ".//li[contains(@class, 'text_type_digits-default')]")
    # 1 заказ в истории
    ORDER_INFO_HISTORY = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem__2x95r')][1]")
    # Все заказы в истории
    ORDERS_HISTORY = (By.XPATH, './/p[contains(@class, "text_type_digits-default")]')
    #Номер заказа
    ORDER_NUMBER = (By.XPATH, './/h2')
    # Крестик на модульном окне
    CLOSE_POPUP_FORM_2 = (By.XPATH, './/div[1]/button')
    # Надпись идентификатор заказа
    ORDER_NUMBER_TEXT = (By.XPATH, './/*[text()="идентификатор заказа"]//ancestor::div[contains(@class, "modal__container")')
