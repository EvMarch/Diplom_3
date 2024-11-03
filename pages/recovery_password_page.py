
from pages.base_page import BasePage
from locators.recovery_page_locators import RecoveryPageLocators
import allure

class RecoveryPage(BasePage):

    @allure.step('Проверка формы восстановления пароля')
    def check_recovery_form(self):
        return self.find_element_located(RecoveryPageLocators.RECOVERY_TEXT)

    @allure.step('Заполнение формы Email')
    def send_email_to_email_field(self, email):
        self.find_element_located(RecoveryPageLocators.EMAIL_INPUT).send_keys(email)

    @allure.step('Нажатие на кнопку Восстановить')
    def click_recovery_btn(self):
        self.find_element_located_click(RecoveryPageLocators.RECOVERY_BUTTON)

    @allure.step('Клик по кнопке Войти')
    def click_login_btn(self):
        self.find_element_located_click(RecoveryPageLocators.LOGIN_BUTTON)

    @allure.step('Заполнение поля Пароль')
    def send_password_to_password_field(self, password):
        self.find_element_located(RecoveryPageLocators.PASSWORD_INPUT).send_keys(password)

    @allure.step('Заполнение поля Код из письма')
    def send_code_to_code_field(self, code):
        self.find_element_located(RecoveryPageLocators.MAIL_CODE_INPUT).send_keys(code)

    @allure.step('Клик по кнопке Сохранить')
    def click_save_btn(self):
        self.find_element_located_click(RecoveryPageLocators.SAVE_BUTTON)

    @allure.step('Проверка подсветки поля Пароль')
    def check_active_password_field(self, password):
        self.send_password_to_password_field(password)
        self.find_element_located(RecoveryPageLocators.SHOW_PASSWORD_BUTTON)
        return self.find_element_located(RecoveryPageLocators.PASSWORD_INPUT_ACTIVE)

    @allure.step('Проверка отображения кнопки Сохранить')
    def check_save_btn(self):
        return self.find_element_located(RecoveryPageLocators.SAVE_BUTTON)