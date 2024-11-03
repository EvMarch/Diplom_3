from faker import Faker
import random
import string
import pytest
from selenium import webdriver

from pages.main_page import MainPage
from pages.login_page import LoginPage
from urls_credits import Urls, Person, Endpoints, Ingredients
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import requests



@pytest.fixture(scope='session')
def wrong_user_password():
    length = random.randint(1, 5)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

@pytest.fixture(params=['chrome', 'firefox'])
def browser(request):
    browser_name = request.param
    driver = None
    if browser_name == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
     #   driver.set_window_size(1920, 1080)
        driver.get(Urls.URL_MAIN)
    elif request.param == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
     #   driver.set_window_size(1920, 1080)
        driver.get(Urls.URL_MAIN)
    else:
        ValueError("Can't create instance for this browser param")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def create_new_user():
    payload = Person.create_data_correct_user()
    response = requests.post(Urls.URL_REGISTRATION, data=payload)
    yield payload, response
    token = response.json()["accessToken"]
    requests.delete(Urls.URL_MAIN + Endpoints.DELETE_USER, headers={"Authorization": token})


@pytest.fixture
def login(browser, create_new_user):
        create_user_data = create_new_user[0]
        header_page = MainPage(browser)
        login_page = LoginPage(browser)
        header_page.click_profile_area_btn()
        login_page.login(create_user_data["email"], create_user_data["password"])
        main_page = MainPage(browser)
        main_page.wait_load_main_page()


@pytest.fixture
def create_order(create_new_user):
    token = create_new_user[1].json()["accessToken"]
    headers = {'Authorization': token}
    response = requests.post(Urls.URL_MAIN + Endpoints.CREATE_ORDER, headers=headers, data=Ingredients.correct_ingredients_data)
    return response.json()["order"]["number"]