import requests
from selenium import webdriver
import pytest
from api_methods import UserMethods, OrderMethods
from curl import MANE_SITE, ApiUrl
from data import Ingredients
from generator import DataCreatedUser


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.set_window_size(1920, 1080)
    driver.get(MANE_SITE)
    yield driver
    driver.quit()

@pytest.fixture
def creating_user():
    user_body = DataCreatedUser.generate_body()
    email = user_body['email']
    password = user_body['password']
    body = UserMethods.creating_user(user_body)
    token = body.json()["accessToken"]
    yield token, email, password
    header = {"Authorization": token}
    UserMethods.delete_user(header)

@pytest.fixture
def creating_user_and_order():
    user_body = DataCreatedUser.generate_body()
    email = user_body['email']
    password = user_body['password']
    body = requests.post(f'{ApiUrl.BASE_URL}{ApiUrl.CREATING_USER_URL}', json=user_body)
    token = body.json()["accessToken"]
    order_body = Ingredients.ingredients_body()
    header = {"Authorization": token}
    OrderMethods.creating_order(header, order_body)
    yield email, password
    UserMethods.delete_user(header)





