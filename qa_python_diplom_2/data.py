import pytest
import allure
from qa_python_diplom_2.generator import Generator



class DataFor:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'

    USER_CREATION = '/api/auth/register'  # ручка создания пользователя
    USER_LOGIN = '/api/auth/login'
    USER_DELETE = '/api/auth/user'
    ORDER_CREATION = '/api/orders'

    #СОЗДАНИЕ ПОЛЬЗОВАТЕЛЯ

    #
    data_for_registration = {"email": Generator.email_generate(6), "password": Generator.password_generate(10), "name": Generator.name_generate(10)}

    data_empty_field = {"email": Generator.email_generate(9), "password": "", "name": Generator.name_generate(10)}
    data_none_field = {"email": Generator.email_generate(9), "name": Generator.name_generate(10)}

    #Если пользователь существует, вернётся код ответа 403 Forbidden.
   # USER_EXIST_ANSWER = {"success": false,
      #  "message": "User already exists"}

    #Если нет одного из полей, вернётся код ответа 403 Forbidden.
   # NONE_FIELD = {"success": false,
      #  "message": "Email, password and name are required fields"}
    #



    #data_of_ingredients
    #0 : "61c0c5a71d1f82001bdaaa6d" "Флюоресцентная булка R2-D3" bun ddd
    #1 : "61c0c5a71d1f82001bdaaa6f" "Мясо бессмертных моллюсков Protostomia" main
    #2 : "61c0c5a71d1f82001bdaaa70" "Говяжий метеорит (отбивная)" main
    #3 : "61c0c5a71d1f82001bdaaa71" "Биокотлета из марсианской Магнолии" main ddd
    #4 : "61c0c5a71d1f82001bdaaa72" "Соус Spicy-X" sauce
    #5 : "61c0c5a71d1f82001bdaaa6e" "Филе Люминесцентного тетраодонтимформа" main
    #6 : "61c0c5a71d1f82001bdaaa73" "Соус фирменный Space Sauce" sauce ddd
    #7 : "61c0c5a71d1f82001bdaaa74" "Соус традиционный галактический" sauce
    #8 : "61c0c5a71d1f82001bdaaa6c" "Краторная булка N-200i" bun
    #9 : "61c0c5a71d1f82001bdaaa75" "Соус с шипами Антарианского плоскоходца" sauce
    #10 : "61c0c5a71d1f82001bdaaa76" "Хрустящие минеральные кольца" main ddd
    #11 : "61c0c5a71d1f82001bdaaa77" "Плоды Фалленианского дерева" main
    #12 : "61c0c5a71d1f82001bdaaa78" "Кристаллы марсианских альфа-сахаридов"
    #13 : "61c0c5a71d1f82001bdaaa79" "Мини-салат Экзо-Плантаго" main
    #14 : "61c0c5a71d1f82001bdaaa7a" "Сыр с астероидной плесенью" main
