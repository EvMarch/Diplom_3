from selenium.webdriver.common.by import By

class PersonalPageLocators:
    # Форма личного кабинета
    PROFILE = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']")
    # Кнопка профиль
    PROFILE_BUTTON = (By.XPATH, ".//a[text() = 'Профиль']")
    # Кнопка история заказов
    HISTORY_BUTTON = (By.XPATH, ".//a[text() = 'История заказов']")
    # Форма истории заказов
    HISTORY_FORM = (By.XPATH, ".//div[@class = 'Account_contentBox__2CPm3']")
    # Номер заказа
    NUMBER_ORDER = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default')]")
    # Кнопка отмена
    CANCEL_BUTTON = (By.XPATH, ".//button[text() = 'Отмена']")
    # Кнопка сохранить
    SAVE_BUTTON = (By.XPATH, ".//button[text() = 'Сохранить']")
    # Кнопка выход
    EXIT_BUTTON = (By.XPATH, ".//button[text() = 'Выход']")
