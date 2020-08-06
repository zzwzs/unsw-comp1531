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
    assert Inventory.buns_list != None
    return Inventory

def testing_list_remove(inventory_fixture):
    Inventory = inventory_fixture
    system = order_system(Inventory)
    
    assert inventory_fixture.drinks_list != []
    system.make_item("seasame buns", 2, 0)
    system.make_item("chicken patties", 2, 0)
    system.make_item("tomato ingredient", 1, 0)
    system.make_sides("nuggets 24pc", 1, 0)
    system.make_sides("mid fries", 1, 0)
    system.make_drinks("cola in can", 2, 0)
    system.make_sundaes("chocolate small", 2, 0)
    assert inventory_fixture.drinks_list[0] != None
    
    system.make_meal(0)
    assert len(system._meals_list) == 1
    system.make_order(0)
    system.append_order(0)
    assert len(system._meals_list) == 0
    assert len(system._item_list) == 0
    assert len(system._drinks_list) == 0
    assert len(system._sides_list) == 0
    assert len(system._sundaes_list) == 0
    
    assert len(system.orders_list) == 1
    assert system.orders_list[0].status == "invalid"
    assert system.orders_list[0].ID == 0
    system.update_status(0)
    assert system.orders_list[0].status == "available"

