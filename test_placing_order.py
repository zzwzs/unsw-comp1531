
import pytest
from order_system import order_system
from Order import order
from inventory_system import Inventory_system
from meals import Meals
from items import Items
from Inventory import *
from combo import *
from combos import *



@pytest.fixture
def inventory_fixture():
    Inventory = Inventory_system()
    Inventory.add_buns(inventory(3, "sesame bun", 20))
    Inventory.add_buns(inventory(3, "muffin bun", 20))
    Inventory.add_patties(inventory(5, "chicken patties", 20))
    Inventory.add_patties(inventory(5, "beef patties", 20))
    Inventory.add_patties(inventory(5, "tomato patties", 20))
    Inventory.add_patties(inventory(5, "lamb patties", 20))
    Inventory.add_ingredient(inventory(2, "tomato sauce", 20))
    Inventory.add_ingredient(inventory(2, "lettuce", 20))
    Inventory.add_ingredient(inventory(2, "cheddar cheese", 20))
    Inventory.add_ingredient(inventory(2, "tomato sauce", 20))
    Inventory.add_drinks(inventory(3, "coke", 20))
    Inventory.add_drinks(inventory(3, "sprite", 20))
    Inventory.add_sides(inventory(3, "fries", 20))
    Inventory.add_sides(inventory(3, "nuggets", 20))
    Inventory.add_sundaes(inventory(3, "chocolate small", 20))
    Inventory.add_sundaes(inventory(4, "chocolate medium", 20))
    Inventory.add_sundaes(inventory(5, "chocolate large", 20))
    Inventory.add_sundaes(inventory(3, "strawberry small", 20))
    Inventory.add_sundaes(inventory(4, "strawberry medium", 20))
    Inventory.add_sundaes(inventory(5, "strawberry large", 20))
    #making double burger
    Inventory.make_a_combo("sesame bun", 2)
    Inventory.make_a_combo("chicken patties", 2)
    Inventory.make_a_combo("beef patties", 1)
    Inventory.make_combo_list
    #making triple burger
    Inventory.make_a_combo("muffin bun", 3)
    Inventory.make_a_combo("chicken patties", 1)
    Inventory.make_a_combo("beef patties", 1)
    Inventory.make_a_combo("lamb patties",1)
    Inventory.make_combo_list
    
    
    return Inventory
       
def test_make_a_double_burger_order(inventory_fixture):
    inventory = inventory_fixture
    system = order_system(inventory)
    order_ID = system.order_ID
    assert order_ID == 0
    assert system.order_ID == 0
    system.make_item("sesame bun", 2, order_ID)
    system.make_item("chicken patties", 1, order_ID)
    system.make_item("lamb patties", 1, order_ID)
    system.make_item("tomato sauce", 2, order_ID)
    system.make_drinks("coke", 1, order_ID)
    system.make_sides("fries", 1, order_ID)
    system.make_sundaes("chocolate small",1, order_ID)
    assert len(system.item_list) == 4
    assert len(system.drinks_list) == 1
    assert len(system.sides_list) == 1
    assert len(system.sundaes_list) == 1
    system.make_meal(order_ID)
    assert len(system.meals_list) == 1
    system.make_order(order_ID)
    #check if the item, drinks,sides, and sundaes list is empty
    assert len(system.item_list) == 0
    assert len(system.drinks_list) == 0
    assert len(system.sides_list) == 0
    assert len(system.sundaes_list) == 0
    assert len(system.meals_list) == 0
    #check if the order list is 1
    assert len(system.unconfirmed_list) == 1
    assert system.unconfirmed_list[0].price == 29
    assert system.unconfirmed_list[0].status == "invalid"
    system.append_order(order_ID) #after checkout
    assert len(system.orders_list) == 1
    assert len(system.unconfirmed_list) == 0
    
    # check status
    assert system.order_info(order_ID) == "invalid"
    
    #update status and check if it is available
    system.update_status(order_ID)
    assert system.orders_list[0].status == "available"
    assert system.order_info(order_ID) == "available"
    
    assert system.int_ordered("tomato sauce", order_ID) == 2
    
    
def test_order_combo(inventory_fixture):
    inventory = inventory_fixture
    assert len(inventory.combo_elements) == 0
    assert len(inventory.combo_list) == 2
    assert inventory.combo_list[0].price == 21
    assert inventory.combo_list[1].price == 24
    
    system = order_system(inventory)
    order_ID = system.order_ID
    assert order_ID == 0
    assert system.order_ID == 0
    assert len(system.meals_list) == 0
    system.choose_combo(0, order_ID)
    assert len(system.drinks_list) == 0
    assert len(system.meals_list) == 1
    system.make_sides("fries", 1, order_ID)
    system.make_sundaes("chocolate small",1, order_ID)
    
    assert len(system.sides_list) == 1
    assert len(system.sundaes_list) == 1
    system.make_order(order_ID)
    assert len(system.meals_list) == 0
    
    assert len(system.unconfirmed_list) == 1
    assert system.unconfirmed_list[0].price == 27
    assert system.unconfirmed_list[0].status == "invalid"
    system.append_order(order_ID) #after checkout
    assert len(system.orders_list) == 1  
    assert len(system.unconfirmed_list) == 0
    
    # check status
    assert system.order_info(order_ID) == "invalid"
    
    #update status and check if it is available
    system.update_status(order_ID)
    assert system.orders_list[0].status == "available"
    assert system.order_info(order_ID) == "available"
    
    assert system.int_ordered("muffin bun", order_ID) == 0
    assert system.int_ordered("sesame bun", order_ID) == 2
    
    pass
            
def test_two_customers(inventory_fixture):
    inventory = inventory_fixture  
    assert len(inventory.combo_elements) == 0
    assert len(inventory.combo_list) == 2
    assert inventory.combo_list[0].price == 21
    assert inventory.combo_list[1].price == 24
    
    system = order_system(inventory)
    
    #customer 1
    order_ID1 = system.order_ID
    assert order_ID1 == 0
    
    
    assert len(system.item_list) == 0
    assert len(system.drinks_list) == 0
    assert len(system.sides_list) == 0
    assert len(system.meals_list) == 0
    assert len(system.sundaes_list) == 0
    assert len(system.unconfirmed_list) == 0
    assert len(system.orders_list) == 0
    
    system.make_item("sesame bun", 3, order_ID1)
    system.make_item("chicken patties", 1, order_ID1)
    system.make_item("lamb patties", 1, order_ID1)
    
    system.make_item("lettuce", 2, order_ID1) 
    system.make_meal(order_ID1)
    assert len(system.item_list) == 0
    assert len(system.meals_list) == 1 
    assert len(system.sides_list) == 0
    
    
    system.make_drinks("coke", 1, order_ID1) # not calculate
    assert len(system.drinks_list) == 1
    
    
    system.make_sides("fries", 1, order_ID1)
    system.make_sides("nuggets", 1, order_ID1)
   
    system.make_sundaes("chocolate small",1, order_ID1)
    system.choose_combo(0, order_ID1)
    system.choose_combo(1, order_ID1)
    
    system.make_drinks("coke", 2, order_ID1)
    
    
    assert len(system.item_list) == 0
    
    assert len(system.sides_list) == 2
    assert len(system.drinks_list) == 1
    assert len(system.meals_list) == 3
    assert len(system.sundaes_list) == 1
    assert len(system.unconfirmed_list) == 0
    assert len(system.orders_list) == 0
    
    system.make_order(order_ID1)
    
    #check if the item, drinks,sides, and sundaes list is empty
    assert len(system.item_list) == 0
    assert len(system.drinks_list) == 0
    assert len(system.sides_list) == 0
    assert len(system.sundaes_list) == 0
    assert len(system.meals_list) == 0
    #check if the order list is 1
    assert len(system.unconfirmed_list) == 1
    for order in system.unconfirmed_list:
        if order.ID == order_ID1:
            assert order.price == 83
            assert order.status == "invalid"
            
            
    system.append_order(order_ID1) #after checkout
    assert len(system.orders_list) == 1
    assert len(system.unconfirmed_list) == 0
    
    # check status
    assert system.order_info(order_ID1) == "invalid"
    
    
    #update status and check if it is available
    system.update_status(order_ID1)
    assert system.order_info(order_ID1) == "available"
   
   
   
    #customer 2
    order_ID2 = system.order_ID
    assert order_ID2 == 1
    system.make_item("sesame bun", 3, order_ID2)
    system.make_item("chicken patties", 1, order_ID2)
    system.make_item("lamb patties", 1, order_ID2)
    system.make_item("lettuce", 2, order_ID2)
    system.make_meal(order_ID2)
    assert len(system.item_list) == 0
    assert len(system.meals_list) == 1 
    assert len(system.sides_list) == 0
    system.choose_combo(1, order_ID2)
    system.choose_combo(1, order_ID2)
    system.make_sides("fries", 1, order_ID2)
    system.make_sundaes("chocolate medium",1, order_ID2)
    assert len(system.item_list) == 0
    
    assert len(system.sides_list) == 1
    assert len(system.drinks_list) == 0
    assert len(system.meals_list) == 3
    assert len(system.sundaes_list) == 1
    assert len(system.unconfirmed_list) == 0
    assert len(system.orders_list) == 1
    
    system.make_order(order_ID2)
    #check if the item, drinks,sides, and sundaes list is empty
    assert len(system.item_list) == 0
    assert len(system.drinks_list) == 0
    assert len(system.sides_list) == 0
    assert len(system.sundaes_list) == 0
    assert len(system.meals_list) == 0
    assert len(system.unconfirmed_list) == 1
    
    for order in system.unconfirmed_list:
        if order.ID == order_ID2:
            assert order.price == 78   
            assert order.status == "invalid"
    system.append_order(order_ID2) #after checkout 
    assert len(system.orders_list) == 2
    assert len(system.unconfirmed_list) == 0
         
    assert system.order_info(order_ID2) == "invalid"  
    system.update_status(order_ID2)
    assert system.order_info(order_ID2) == "available"
    
    assert system.int_ordered("lettuce", order_ID2) == 2
    
    
    
    
    
    
    
    
    
    
    
    
    
    

