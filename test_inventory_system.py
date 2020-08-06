import pytest

from order_system import order_system
from Order import order
from inventory_system import Inventory_system
from meals import Meals
from items import Items
from Inventory import *



@pytest.fixture
def inventory_fixture():
    Inventory = Inventory_system()
    Inventory.add_buns(inventory(5, "seasame buns", 10))
    Inventory.add_buns(inventory(3, "muffin buns", 15))
    Inventory.add_patties(inventory(5, "chicken patties", 10))
    Inventory.add_patties(inventory(11, "pork patties", 17))
    Inventory.add_sides(inventory(12, "nuggets 24pc", 80))
    Inventory.add_sides(inventory(2, "mid fries", 80))
    Inventory.add_ingredient(inventory(1, "tomato ingredient", 800))
    Inventory.add_ingredient(inventory(1, "pickle ingredient", 500))
    Inventory.add_drinks(inventory(2.5, "cola in can", 80))
    Inventory.add_drinks(inventory(3.5, "cola in bottle", 85))
    Inventory.add_sundaes(inventory(3, "chocolate small", 100))
    Inventory.add_sundaes(inventory(4, "chocolate medium", 100))
    Inventory.add_sundaes(inventory(5, "chocolate large", 100))
    Inventory.add_sundaes(inventory(3, "strawberry small", 100))
    Inventory.add_sundaes(inventory(4, "strawberry medium", 100))
    Inventory.add_sundaes(inventory(5, "strawberry large", 100))
    return Inventory
    
def testing_inventory(inventory_fixture):
    Inventory = inventory_fixture
    assert Inventory.buns_list != None
    assert Inventory.patties_list != None
    assert Inventory.sides_list != None
    assert Inventory.ingredient_list != None
    assert Inventory.drinks_list != None
    assert Inventory.sundaes_list != None
    
    assert len(Inventory.buns_list) == 2
    assert len(Inventory.patties_list) == 2
    assert len(Inventory.sides_list) == 2
    assert len(Inventory.ingredient_list) == 2
    assert len(Inventory.drinks_list) == 2
    assert len(Inventory.sundaes_list) == 6



