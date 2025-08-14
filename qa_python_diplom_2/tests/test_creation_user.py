import pytest
import allure
import requests
from qa_python_diplom_2.data import DataFor
from qa_python_diplom_2.conftest import *



class TestCreationUser:

    @allure.title('Проверка создания пользователя')
    @allure.description('При отправке тела запроса со всеми валидными необходимыми полями происходит создание пользователя')
    def test_creation_user_positive_flow(self, user_creation):
        with allure.step('Отправка валидных данных для создания пользователя'):
            response = requests.post(f'{DataFor.BASE_URL}{DataFor.USER_CREATION}', json=user_creation)
        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 200


    @allure.title('Проверка создания уже зарегистрированного пользователя')
    @allure.description('При попытке создания уже зарегистрированного пользователя всплывает сообщение об ошибке')
    def test_creation_double_user_raise_error(self, user_creation):
        with allure.step('Отправка валидных данных для создания пользователя'):
            response = requests.post(f'{DataFor.BASE_URL}{DataFor.USER_CREATION}', json=user_creation)
        with allure.step('Попытка зарегистрировать второго такого же пользователя'):
            if response.status_code == 200:
                response = requests.post(f'{DataFor.BASE_URL}{DataFor.USER_CREATION}', json=user_creation)
            else:
                pass
        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 403


    @allure.title('Тест создания пользователя с пустым обязательным полем')
    @allure.title('Проверка, что при попытке создания пользователя с пустым одним из обязательных полей возвращается ошибка')
    def test_creation_empty_fields_user_raise_error(self):
        with allure.step('Отправка запроса на создание пользователя с пустым паролем'):
            response = requests.post(f'{DataFor.BASE_URL}{DataFor.USER_CREATION}', json=DataFor.data_empty_field)
        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 403


    @allure.title('Тест создания пользователя с отсутствующим одним из обязательных полей')
    @allure.description('Проверка, что при попытке создания пользователя с отсутствующим одним из обязательных полей возвращается ошибка')
    def test_creation_none_field_user_raise_error(self):
        with allure.step('Отправка запроса на создание пользователя с отсутствующим полем'):
            response = requests.post(f'{DataFor.BASE_URL}{DataFor.USER_CREATION}', json=DataFor.data_none_field)
        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 403




