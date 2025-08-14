import pytest
from praktikum.burger import Burger
from unittest.mock import Mock

@pytest.fixture()
def burger():
    burger = Burger()
    return burger

@pytest.fixture()
def bun():
    bun_mock = Mock()
    bun_mock.get_name.return_value = "Space bun"
    bun_mock.get_price.return_value = 50.0
    return bun_mock

@pytest.fixture()
def ingredient():
    ingredient_mock = Mock()
    ingredient_mock.get_price.return_value = 75.0
    ingredient_mock.get_name.return_value = "Space beef"
    ingredient_mock.get_type.return_value = "FILLING"
    return ingredient_mock
