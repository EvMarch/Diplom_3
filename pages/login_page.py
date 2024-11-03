import allure
from pages.base_page import BasePage
from locators.auth_page_locators import AuthPageLocators


class LoginPage(BasePage):

    @allure.step('Проверка отображения формы логина')
    def check_authorization_form_verification(self):
        return self.find_element_located(AuthPageLocators.AUTH_FORM)

    @allure.step('Заполнение поля "Email"')
    def send_email_to_email_field(self, email):
        self.find_element_located(AuthPageLocators.EMAIL_INPUT).send_keys(email)

    @allure.step('Заполнение поля "Password"')
    def send_password_to_password_field(self, password):
        self.find_element_located(AuthPageLocators.PASSWORD_INPUT).send_keys(password)

    @allure.step('Клик на кнопку "Войти"')
    def click_login_btn(self):
        self.move_to_element_and_click(AuthPageLocators.LOGIN_BUTTON)

    @allure.step('Авторизация на сайте')
    def login(self, email, password):
        self.send_email_to_email_field(email)
        self.send_password_to_password_field(password)
        self.click_login_btn()

    @allure.step('Клик на кнопку "Восстановить пароль"')
    def click_recovery_btn(self):
        self.move_to_element_and_click(AuthPageLocators.RECOVER_BUTTON)

    @allure.step('Клик на кнопку "Зарегистрироваться"')
    def click_register_btn(self):
        self.move_to_element_and_click(AuthPageLocators.REGISTRATION_BUTTON)