from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from conftest_delete import ingredient


class TestBurger:

    def test_set_buns(self, bun, burger):
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self, ingredient, burger):
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.add_ingredients[0] == ingredient

    def test_remove_ingredient(self, ingredient, burger):
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 2
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self, burger):
        ingredient_1 = Mock()
        ingredient_2 = Mock()
        ingredient_1.get_name.return_value = "Beef"
        ingredient_2.get_name.return_value = "Sauce"

        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient_2, ingredient_1]




    def test_get_price(self, burger, bun):
        burger.set_buns(bun)
        beef = Ingredient("FILLING", "Space Beef", 50.0)
        sauce = Ingredient("SAUCE", "Space sause", 25.0)
        burger.add_ingredient(beef)
        burger.add_ingredient(sauce)
        assert burger.get_price() == 175.0


    def test_get_receipt(self, burger, bun, ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        expected_receipt = f'= {ingredient.get_type().lower()} {ingredient.get_name()} =\n'\
        f'(==== {burger.bun.get_name()} ====)\n'\
        f'Price: {burger.get_price()}'
        assert burger.get_receipt() == expected_receipt



