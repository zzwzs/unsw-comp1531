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
    Inventory.make_a_combo("seasame buns", 2)
    Inventory.make_a_combo("chicken patties", 1)
    Inventory.make_a_combo("pickle ingredient", 1)
    Inventory.make_combo_list()
    Inventory.make_a_combo("muffin buns", 2)
    Inventory.make_a_combo("pork patties", 1)
    Inventory.make_a_combo("tomato ingredient", 1)
    Inventory.make_combo_list()
    
    #assert len(Inventory.combo_list) == 1
    assert Inventory.combo_list[0] != None
    assert Inventory.buns_list != None
    return Inventory

def testing_price_calc(inventory_fixture):
    print("testing_one_customer_order")
    Inventory = inventory_fixture
    system = order_system(Inventory)
    
    '''
    if 
    system
    '''
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
    assert len(system.orders_list) == 1
    assert system.orders_list[0].price == 46
    
    system.make_item("muffin buns", 3, 1)
    system.make_item("pork patties", 1, 1)
    system.make_item("tomato ingredient", 2, 1)
    system.make_item("pickle ingredient", 2, 1)
    system.make_sides("mid fries", 2, 1)
    system.make_drinks("cola in can", 1, 1)
    system.make_drinks("cola in bottle", 2, 1)
    system.make_sundaes("chocolate small", 1, 1)
    system.make_sundaes("strawberry medium", 1, 1)
    system.make_sundaes("strawberry large", 3, 1)
    assert inventory_fixture.drinks_list[1] != None
    
    system.make_meal(1)
    assert len(system._meals_list) == 1
    system.make_order(1)
    system.append_order(1)
    assert len(system._meals_list) == 0
    assert len(system.orders_list) == 2
    assert system.orders_list[1].price == 59.5
    
    system.make_sides("nuggets 24pc", 1, 2)
    system.make_sides("mid fries", 1, 2)
    system.make_drinks("cola in can", 2, 2)
    system.make_sundaes("chocolate small", 2, 2)
    
    system.choose_combo(0, 2)
    system.make_meal(2)
    system.make_order(2)
    system.append_order(2)
    assert system.orders_list[2].price == 41
