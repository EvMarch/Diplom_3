from faker import Faker
import random
import string
import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def user_name():
#Генерирует имя
    name = Faker(['en_US']).first_name()
    return name

@pytest.fixture(scope='session')
def user_email(user_name, domain="yandex.ru"):
    user_name = user_name.lower()  # Имя в нижнем регистре
    surname = Faker(['en_US']).last_name().lower()  # Фамилия в нижнем регистре
    kogorta_number = random.randint(1, 10)  # Случайное число от 100 до 999
    unique_number = random.randint(100, 999)  # Случайное число от 100 до 999
    email = f"{user_name}_{surname}_str{kogorta_number}_{str(unique_number)}@{domain}"  # Форматирование почты
    return email


@pytest.fixture(scope='session')
def user_password(length=6):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

@pytest.fixture(scope='session')
def wrong_user_password():
    length = random.randint(1, 5)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()