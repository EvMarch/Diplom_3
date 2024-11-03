from selenium.webdriver.common.by import By

class RecoveryPageLocators:

    # поле почты
    EMAIL_INPUT = (By.XPATH, ".//input[@name = 'name']")

    # Кнопка Восстановить
    RECOVERY_BUTTON = (By.XPATH, ".//button[text() = 'Восстановить']")
    # Кнопка Войти
    LOGIN_BUTTON = (By.XPATH, ".//a[text() = 'Войти']")
    # Поле ввода нового пароля
    PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Введите новый пароль']")
    # Поле ввода кода из письма
    MAIL_CODE_INPUT = (By.XPATH, ".//label[text() = 'Введите код из письма']")
    # Кнопка Сохранить
    SAVE_BUTTON = (By.XPATH, ".//button[text() = 'Сохранить']")
    # Заголовок восстановления пароля
    RECOVERY_TEXT = (By.XPATH, ".//h2[text() = 'Восстановление пароля']")
    # Показать пароль
    SHOW_PASSWORD_BUTTON = (By.XPATH, ".//div[@class = 'input__icon input__icon-action']")
    # Подсветка поля пароль
    PASSWORD_INPUT_ACTIVE = (By.CSS_SELECTOR, ".input.input_status_active")

