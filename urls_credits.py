import allure
from faker import Faker

class Urls:

    URL_REGISTRATION = "https://stellarburgers.nomoreparties.site/register"
    URL_MAIN = "https://stellarburgers.nomoreparties.site/"
    URL_LOGIN = "https://stellarburgers.nomoreparties.site/login"
    URL_FORGOT_PASSWORD = "https://stellarburgers.nomoreparties.site/forgot-password"
    URL_RECOVERY_PASSWORD = "https://stellarburgers.nomoreparties.site/reset-password"
    URL_PROFILE = "https://stellarburgers.nomoreparties.site/account/profile"
    URL_HISTORY = "https://stellarburgers.nomoreparties.site/account/order-history"


class Endpoints:

    CREATE_USER = 'api/auth/register'
    LOGIN = 'api/auth/login'
    DELETE_USER = 'api/auth/user'
    CREATE_ORDER = 'api/orders'
    GET_ORDERS = 'api/orders'


class Credits:

    LOGIN_USER='testtestov'
    EMAIL_USER='testtestov4444@yandex.ru'
    PASSWORD_USER='123456'

class Person:

    @staticmethod
    @allure.step('Генерация email, password, name пользователя')
    def create_data_correct_user():
        faker = Faker('ru_RU')
        data = {
            "email": faker.email(),
            "password": faker.password(),
            "name": faker.first_name()
        }
        return data

class Ingredients:

    correct_ingredients_data = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
        }