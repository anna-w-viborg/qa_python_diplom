import allure
import pytest
import requests
from qa_python_diplom_2.conftest import *

class TestOrderCreation:

    @allure.title('Тест создания заказа с авторизацией с пререданными ингредиентами')
    @allure.description('Проверка, что если авторизованный пользователь оформляет заказ с указанием ингредиентов в теле запроса, заказ оформляется')
    def test_order_creation_with_authorization(self, user_authorization):
        with allure.step('Отправка запроса на авторизацию пользователя'):
            response = requests.post(f'{DataFor.BASE_URL}{DataFor.USER_LOGIN}', json=user_authorization)
        with allure.step('Получение токена пользователя'):
            token = response.json().get("accessToken")
        with allure.step('Если пользователь авторизован, переходим к созданию заказа'):
            if response.status_code == 200 and "accessToken" in response.json():
                order_data = {"ingredients" : ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa71", "61c0c5a71d1f82001bdaaa73", "61c0c5a71d1f82001bdaaa76", "61c0c5a71d1f82001bdaaa6c"] }
                headers = {"Authorization": f"Bearer {token}"}
                response = requests.post(f'{DataFor.BASE_URL}{DataFor.ORDER_CREATION}', json=order_data, headers=headers)
        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 200 and "order" in response.json()

    @allure.title('Тест создание заказа без авторизации')
    @allure.description('Проверка, что невозможно создать заказ, не будучи авторизованным пользователем')
    def test_order_creation_without_authorization(self):
        with allure.step('Создание словаря для подставление в тело запроса оформления заказа'):
            order_data = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa71", "61c0c5a71d1f82001bdaaa73",
                            "61c0c5a71d1f82001bdaaa76", "61c0c5a71d1f82001bdaaa6c"]}
        with allure.step('Отправка запроса на создание заказа'):
            response = requests.post(f'{DataFor.BASE_URL}{DataFor.ORDER_CREATION}', json=order_data)
        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 400

    @allure.title('Тест создание заказа без ингредиентов')
    @allure.description('Проверка, что при попытке создания заказа без ингредиентов в ответ приходит ошибка')
    def test_order_creation_without_ingredients(self, user_authorization):
        with allure.step('Отправление запроса для авторизации пользователя'):
            response = requests.post(f'{DataFor.BASE_URL}{DataFor.USER_LOGIN}', json=user_authorization)
        with allure.step('Получение токена пользователя'):
            token = response.json().get("accessToken")
        with allure.step('Если пользователь авторизован, пытаемся оформить заказ без ингредиентов'):
            if response.status_code == 200 and "accessToken" in response.json():
                order_data = {"ingredients" : [] }
                headers = {"Authorization": f"Bearer {token}"}
                response = requests.post(f'{DataFor.BASE_URL}{DataFor.ORDER_CREATION}', json=order_data, headers=headers)
        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 500

    @allure.title('Тест создания заказов с неверным id ингредиентов')
    @allure.description('Проверка, что при передаче в тело запроса ингредиентов с неверным id всплывает ошибка')
    def test_order_creation_with_the_wrong_id_ingredients(self, user_authorization):
        with allure.step('Отправка запроса на авторизацию пользователя'):
            response = requests.post(f'{DataFor.BASE_URL}{DataFor.USER_LOGIN}', json=user_authorization)
        with allure.step('Получения токена доступа пользователя'):
            token = response.json().get("accessToken")
        with allure.step('Если пользователь авторизован, переходим к созданию заказа'):
            if response.status_code == 200 and "accessToken" in response.json():
                order_data = {"ingredients" : ["61c0c5a71d1f82001bdaaagh", "61c0c5a71d1f82001bdaaalk", "61c0c5a71d1f82001bdaaa11", "61c0c5a71d1f82001bdaaa22", "61c0c5a71d1f82001bdaaa00"] }
                headers = {"Authorization": f"Bearer {token}"}
                response = requests.post(f'{DataFor.BASE_URL}{DataFor.ORDER_CREATION}', json=order_data, headers=headers)
        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 500

