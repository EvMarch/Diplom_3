from selenium.webdriver.common.by import By

class RecoveryPageLocators:

    # поле почты
    EMAIL_INPUT = ".//label[contains(text(), 'Email')]/following-sibling::input"

    # кнопка восстановить
    RECOVERY_RASSWORD_BUTTON = "//p[text() = 'Личный Кабинет']"

