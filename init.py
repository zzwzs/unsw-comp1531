from order_system import order_system
from Order import order
from inventory_system import Inventory_system
from meals import Meals
from items import Items
from Inventory import *

def boots_system():
    Inventory = Inventory_system()
    Inventory.add_buns(inventory(2, "seasame_buns", 10000))
    Inventory.add_buns(inventory(3, "muffin_buns", 15000))
    
    Inventory.add_patties(inventory(5, "chicken_patties", 10000))
    Inventory.add_patties(inventory(4, "pork_patties", 15000))
    Inventory.add_patties(inventory(6, "beef_patties", 17000))
    Inventory.add_patties(inventory(4, "vegetarian_patties", 17000))
    
    Inventory.add_sides(inventory(12, "nuggets", 80000))
    Inventory.add_sides(inventory(6, "fries", 8000000))
    
    Inventory.add_ingredient(inventory(1, "tomato_sauce", 8003244))
    Inventory.add_ingredient(inventory(1, "cheddar_cheese", 50342340))
    Inventory.add_ingredient(inventory(1, "swiss_cheese", 5034240))

    Inventory.add_drinks(inventory(5, "coke", 8000))
    Inventory.add_drinks(inventory(5, "small_chocolate_sundaes", 8000))
    Inventory.add_drinks(inventory(5, "large_chocolate_sundaes", 8000))
    Inventory.add_drinks(inventory(5, "sprite", 8500))
    Inventory.add_drinks(inventory(6, "apple_julice", 8000))
    Inventory.add_drinks(inventory(6, "orange_julice", 8500))
    
    Inventory.add_sundaes(inventory(3, "chocolate small", 10000))
    Inventory.add_sundaes(inventory(4, "chocolate medium", 10000))
    Inventory.add_sundaes(inventory(5, "chocolate large", 10000))
    Inventory.add_sundaes(inventory(3, "strawberry small", 10021))
    Inventory.add_sundaes(inventory(4, "strawberry medium", 10042))
    Inventory.add_sundaes(inventory(5, "strawberry large", 10041))

    Inventory.make_a_combo("seasame_buns", 2)
    Inventory.make_a_combo("pork_patties", 2)
    Inventory.make_a_combo("tomato_sauce", 1)
    Inventory.make_combo_list
    
    Inventory.make_a_combo("seasame_buns", 2)
    Inventory.make_a_combo("chicken_patties", 3)
    Inventory.make_a_combo("tomato_sauce", 1)
    Inventory.make_combo_list

    Inventory.make_a_combo("muffin_buns", 2)
    Inventory.make_a_combo("pork_patties", 3)
    Inventory.make_a_combo("tomato_sauce", 1)
    Inventory.make_combo_list

    Inventory.make_a_combo("muffin_buns", 2)
    Inventory.make_a_combo("chicken_patties", 3)
    Inventory.make_a_combo("tomato_sauce", 1)
    Inventory.make_combo_list

    system = order_system(Inventory)
    return system
