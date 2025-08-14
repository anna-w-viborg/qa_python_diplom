import pytest
import allure
import requests
from qa_python_diplom_2.data import DataFor
from qa_python_diplom_2.conftest import *

class TestLoginUser:

    @allure.title('Тест логина пользователя')
    @allure.description('Проверка, что при правильной передаче обязательных полей в теле запроса происходит успешная авторизация')
    def test_login_user_positive_flow(self, user_authorization):
        with allure.step(''):
            response = requests.post(f'{DataFor.BASE_URL}{DataFor.USER_LOGIN}', json=user_authorization)
        with allure.step(''):
            token = response.json().get("accessToken")
        with allure.step(''):
            assert response.status_code == 200 and "accessToken" in response.json()




    @allure.title('Тест логин с неправильным логином')
    @allure.description('Проверка, что при неправильном логине, переданном в теле запроса на авторизацию, возвращается ошибка')
    def test_login_user_wrong_login(self):
        with allure.step('Генерация данных для создания пользователя'):
            email = Generator.email_generate(10)
            password = Generator.password_generate(10)
            name = Generator.name_generate(10)
        with allure.step('Создание словаря для подставления в тело запроса создания пользователя'):
            creation_body = {"email": email, "password": password, "name": name}
        with allure.step('Отправка запроса на создание пользователя'):
            response = requests.post(f'{DataFor.BASE_URL}{DataFor.USER_CREATION}', json=creation_body)
        with allure.step('Если пользователь успешно создан, переходим к логину с неправильным логином'):
            if response.status_code == 200:
                wrong_body = {"email": Generator.email_generate(6), "password": password,}
                response = requests.post(f'{DataFor.BASE_URL}{DataFor.USER_LOGIN}', json=wrong_body)
        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 401


    @allure.title('Тест логин с неправильным паролем')
    @allure.description('Проверка, что при передаче неправильного пароля в теле запроса на авторизацию, приходит сообщение об ошибке')
    def test_login_user_wrong_password(self):
        with allure.step('Генерация данных для создания пользователя'):
            email = Generator.email_generate(10)
            password = Generator.password_generate(10)
            name = Generator.name_generate(10)
        with allure.step('Создание словаря для подставления в тело запроса создания пользователя'):
            creation_body = {"email": email, "password": password, "name": name}
        with allure.step('Отправка запроса на создание пользователя'):
            response = requests.post(f'{DataFor.BASE_URL}{DataFor.USER_CREATION}', json=creation_body)
        with allure.step('Если пользователь успешно создан, переходим к логину с неправильным паролем'):
            if response.status_code == 200:
                wrong_body = {"email": email, "password": Generator.password_generate(6), }
                response = requests.post(f'{DataFor.BASE_URL}{DataFor.USER_LOGIN}', json=wrong_body)
        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 401


