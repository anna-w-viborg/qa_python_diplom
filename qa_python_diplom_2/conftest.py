import pytest
import requests
import allure
import allure_pytest
from qa_python_diplom_2.generator import Generator
from qa_python_diplom_2.data import DataFor

@pytest.fixture()
def user_creation():
    with allure.step('Генерация данных для создания пользователя'):
        email = Generator.email_generate(10)
        password = Generator.password_generate(10)
        name = Generator.name_generate(10)
    with allure.step('Создание словаря для подставления в тело запроса создания пользователя'):
        creation_body = {"email": email, "password": password, "name": name}
    yield creation_body
    with allure.step('Создание словаря для подставления в тело запроса авторизации пользователя'):
        login_body = {"email": email, "password": password}
    with allure.step('Получение токена доступа для пользователя'):
        response = requests.post(f'{DataFor.BASE_URL}{DataFor.USER_LOGIN}', json=login_body)
        token = response.json().get("accessToken")
    with allure.step('Удаление созданного пользователя после проведенного теста'):
        response = requests.delete(f'{DataFor.BASE_URL}{DataFor.USER_DELETE}', headers={"Authorization": f"Bearer {token}"})


@pytest.fixture()
def user_authorization():
    with allure.step('Генерация данных для создания пользователя'):
        email = Generator.email_generate(10)
        password = Generator.password_generate(10)
        name = Generator.name_generate(10)
    with allure.step('Создание словаря для подставления в тело запроса создания пользователя'):
        creation_body = {"email": email, "password": password, "name": name}
    with allure.step('Отправка запроса на создание пользователя'):
        response = requests.post(f'{DataFor.BASE_URL}{DataFor.USER_CREATION}', json=creation_body)
    with allure.step('Создание словаря для подставления в тело запроса авторизации пользователя'):
        login_body = {"email": email, "password": password}
        yield login_body
    with allure.step('Удаление созданного пользователя после проведенного теста'):
        response = requests.post(f'{DataFor.BASE_URL}{DataFor.USER_LOGIN}', json=login_body)
        token = response.json().get("accessToken")
        response = requests.delete(f'{DataFor.BASE_URL}{DataFor.USER_DELETE}', headers={"Authorization": f"Bearer {token}"})


def courier_creation():
    with allure.step('Генерация данных для создания курьера'):
        login = Generator.login_generate(10)
        password = Generator.password_generate(10)
        name = Generator.password_generate(10)
    with allure.step('Создание словаря для подставления в тело запроса создания курьера'):
        creation_body = {"login":login, "password":password, "firstName":name}
    with allure.step('Создание словаря для подставления в тело запроса авторизации курьера'):
        login_body = {"login":login, "password":password}
    yield creation_body
    with allure.step('Авторизация созданного курьера для удаления после завершения теста'):
        login_in = requests.post(f"{Urls.MAIN_URL}{Urls.COURIER_LOGIN_HANDLE}", json=login_body)
    with allure.step('Игнорирование удаления курьера в случае ошибки и невозможности удалить'):
        if login_in.status_code == 200:
            try:
                response_data = login_in.json()
                if "id" in response_data:
                    courier_id = response_data["id"]
                    requests.delete(f'{Urls.MAIN_URL}{Urls.COURIER_DELETE_HANDLE}{courier_id}')
            except KeyError:
                pass