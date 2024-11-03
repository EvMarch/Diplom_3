from selenium.webdriver.common.by import By

class AuthPageLocators:
    # Форма авторизации
    AUTH_FORM = (By.XPATH, ".//div[@class = 'Auth_login__3hAey']")
    # Поле ввода email
    EMAIL_INPUT = (By.XPATH, ".//input[@name = 'name']")
    ## Поле ввода пароля
    PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Пароль']")
    # Кнопка войти
    LOGIN_BUTTON = (By.XPATH, "//button[text() = 'Войти']")
    # Кнопка зерегистрироваться
    REGISTRATION_BUTTON = (By.XPATH, "//a[text() = 'Зарегистрироваться']")
    # Кнопка восстановить пароль
    RECOVER_BUTTON = (By.XPATH, "//a[text() = 'Восстановить пароль']")