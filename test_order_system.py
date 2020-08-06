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

def testing_one_customer_order(inventory_fixture):
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
    assert system.orders_list[0].price == 46
    
    assert len(system.orders_list) == 1
    assert system.orders_list[0].status == "invalid"
    assert system.orders_list[0].ID == 0
    #assert system.total_calc(0) == None
    #assert system._total_p == 38
    system.update_status(0)
    assert system.orders_list[0].status == "available"

def testing_two_customer_order(inventory_fixture):
    print("testing_one_customer_order")
    Inventory = inventory_fixture
    system = order_system(Inventory)
    system.make_item("seasame buns", 2, 0)
    system.make_item("chicken patties", 2, 1)
    system.make_item("tomato ingredient", 1, 0)
    system.make_sides("nuggets 24pc", 1, 1)
    system.make_drinks("cola in can", 2, 0)
    system.make_item("seasame buns", 2, 1)
    system.make_item("chicken patties", 2, 0)
    system.make_item("tomato ingredient", 1, 1)
    system.make_sides("nuggets 24pc", 1, 0)
    system.make_drinks("cola in can", 2, 1)
    
    system.make_meal(0)
    assert len(system.meals_list) == 1
    system.make_order(0)
    assert len(system.meals_list) == 0
    system.append_order(0)
    assert len(system.orders_list) == 1
    assert system.orders_list[0].status == "invalid"
    assert system.orders_list[0].ID == 0
    
    system.make_meal(1)
    assert len(system.meals_list) == 1
    system.make_order(1)
    system.append_order(1)
    assert len(system.meals_list) == 0
    
    assert len(system.orders_list) == 2
    assert system.orders_list[1].status == "invalid"
    assert system.orders_list[1].ID == 1

def testing_one_customer_two_order(inventory_fixture):
    print("testing_one_customer_order")
    Inventory = inventory_fixture
    system = order_system(Inventory)
    system.make_item("seasame buns", 2, 0)
    system.make_item("chicken patties", 2, 0)
    system.make_item("tomato ingredient", 1, 0)
    
    system.make_meal(0)
    assert len(system.meals_list) == 1
    
    system.make_sides("nuggets 24pc", 1, 0)
    system.make_drinks("cola in can", 2, 0)
    
    assert len(system.drinks_list) == 1
    assert len(system.sides_list) == 1
    
    system.make_item("seasame buns", 2, 0)
    system.make_item("chicken patties", 2, 0)
    system.make_item("tomato ingredient", 1, 0)
    
    system.make_meal(0)
    assert len(system.meals_list) == 2
    

    system.make_sides("mid fries", 1, 0)
    system.make_drinks("cola in can", 2, 0)
    assert len(system.drinks_list) == 1
    assert len(system.sides_list) == 2

    system.make_order(0)
    
    assert len(system.drinks_list) == 0
    assert len(system.sides_list) == 0
    assert len(system.meals_list) == 0
    system.append_order(0)
    assert len(system.orders_list) == 1
    assert system.orders_list[0].status == "invalid"
    assert system.orders_list[0].ID == 0
