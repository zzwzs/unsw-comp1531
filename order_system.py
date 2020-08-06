from Order import order
from inventory_system import Inventory_system
from meals import Meals
from items import Items
from combo import Combo
from Inventory import *

inventory = Inventory_system()

class order_system():

    def __init__(self, inventory_system):
        self._orders_list = []
        self._orders_list_unconfirmed = []
        self._item_list = []
        self._meals_list = []
        self._drinks_list = []
        self._sides_list = []
        self._sundaes_list = []
        self._combo_list = inventory_system.combo_list
        self._inventory_system = inventory_system
        self._total_p = 0
        self._order_ID = 0

   
        
    def make_item(self, name, num, order_ID):
        if num < 0:
            print("error")
            return None
        for buns in inventory.buns_list:
            if buns.itemName == name:
                if num < 2:
                    print("The number of buns should be at least 2!")   # check if the number of buns is within 2 and 4
                    return None
                if num > 4:
                    print("buns chosed exceed the maximum amount!")
                    return None
        
        new_itemlll = []
        
        for i in self._item_list:
            new_itemlll.append(i)
        
        for i in new_itemlll:
            if i.name == name and i.order_ID == order_ID:   # if the item has already exist in the item_list, remove the old one
                self._item_list.remove(i)
        
                     
        
        item = Items(name, num, order_ID)

        self._item_list.append(item)  
        return 0

    
    def make_drinks(self, name, num, order_ID):
        if num < 0 or num == 0:
            print("error")
            return None 
        #assert name == "cola in can"
       
        inven_drink = self._inventory_system.search_item(name)
        if num > inven_drink.inventoryNum:
            print("error! {0} exceed the available amount! Please enter again.".format(name))   #check the drinks inventory
            return None
            
        new_itemlll = []
        
        for i in self._drinks_list:
            new_itemlll.append(i)
        
        for i in new_itemlll:
            if i.name == name and i.order_ID == order_ID:  #delete the drink already in the drinks_list
                self._drinks_list.remove(i)      
        item = Items(name, num, order_ID)
        self._drinks_list.append(item) 
        
    def make_sides(self, name, num, order_ID):
        if num < 0:
            print("error")
            return None   
        inven_side = self._inventory_system.search_item(name)
        if num > inven_side.inventoryNum:
            print("error! {0} exceed the available amount! Please enter again.".format(name))  #check the sides inventory
            return None
            
        new_itemlll = []
        
        for i in self._sides_list:
            new_itemlll.append(i)
        
        for i in new_itemlll:
            if i.name == name and i.order_ID == order_ID:  #delete the drink already in the drinks_list
                self._sides_list.remove(i)
                    
        item = Items(name, num, order_ID)
        self._sides_list.append(item)       
            
    
    def make_sundaes(self, name, num, order_ID):
        if num < 0:
            print("error")
            return None   
        inven_sundaes = self._inventory_system.search_item(name)
        if num > inven_sundaes.inventoryNum:
            print("error! {0} exceed the available amount! Please enter again.".format(name))  #check the sides inventory
            return None
            
        new_itemlll = []
        
        for i in self._sundaes_list:
            new_itemlll.append(i)
        
        for i in new_itemlll:
            if i.name == name and i.order_ID == order_ID:  #delete the drink already in the drinks_list
                self._sundaes_list.remove(i)
            
        item = Items(name, num, order_ID)
        self._sundaes_list.append(item) 
               
            
    def make_meal(self, order_ID):
        new_item_list = []
        for i in self._item_list:
            if i.order_ID == order_ID:
                item1 = self._inventory_system.search_item(i.name)
                
                if i.num > item1.inventoryNum:
                    print("error! {0} exceed the available amount! Please enter again.".format(item.name))   #check the meals inventory
                    return None
                new_item_list.append(i)
             
        
        new_itemlll = []
        
        for i in self._item_list:
            new_itemlll.append(i)
        
        for i in new_itemlll:
            if i.order_ID == order_ID:
                self._item_list.remove(i)                        
        
        meal = Meals(new_item_list,order_ID)   #check
        self._meals_list.append(meal)
            
        
 
       
    def make_order(self, order_ID):  
        new_order_list = []  # make a new list to store a list of meals and drinks and sides in one particular order
        price_drink = 0
        price_meal = 0
        price_side = 0
        price_sundaes = 0
        
        #calculate the price of meals
        if len(self._meals_list) != 0:
            for meals in self._meals_list:
                if meals.order_ID == order_ID:
                    new_order_list.append(meals)
                    for mealss in meals.meal:
                        itemss = self._inventory_system.search_item(mealss.name)
                        if itemss != None:
                            price_meal = price_meal + mealss.num * itemss.itemPrice
                        else:
                            price_meal = 0
                    
        new_itemlll = []
        
        for i in self._meals_list:
            new_itemlll.append(i)
        
        for i in new_itemlll:
            if i.order_ID == order_ID:
                self._meals_list.remove(i) 
                
             
                
        #calculate price of drinks
        if len(self._drinks_list) != 0:        
            for drink in self._drinks_list:
                if drink.order_ID == order_ID:
                    new_order_list.append(drink)
                    drinkss = self._inventory_system.search_item(drink.name)
                    if drinkss != None:
                        price_drink = price_drink + drinkss.itemPrice * drink.num
                    else:
                        price_drink = 0
                    
                    
            new_itemlll = []
        
            for i in self._drinks_list:
                new_itemlll.append(i)
            
            for i in new_itemlll:
                if i.order_ID == order_ID:
                    self._drinks_list.remove(i)
                
        #calculate the price of side
        if len(self._sides_list) != 0:
            for side in self._sides_list:
                if side.order_ID == order_ID:
                    new_order_list.append(side)
                    sidess = self._inventory_system.search_item(side.name)
                    if sidess != None:
                        price_side = price_side + sidess.itemPrice * side.num
                    else:
                        price_side = 0
                    

            new_itemlll = []
        
            for i in self._sides_list:
                new_itemlll.append(i)
            
            for i in new_itemlll:
                if i.order_ID == order_ID:
                    self._sides_list.remove(i)
                 
        if len(self._sundaes_list) != 0:                       
            for sundaes in self._sundaes_list:
                if sundaes.order_ID == order_ID:
                    new_order_list.append(sundaes)
                    sundaess = self._inventory_system.search_item(sundaes.name)
                    if sundaess != None:
                        price_sundaes = price_sundaes + sundaess.itemPrice * sundaes.num
                    else:
                        price_sundaes = 0
                    

            new_itemlll = []
        
            for i in self._sundaes_list:
                new_itemlll.append(i)
            
            for i in new_itemlll:
                if i.order_ID == order_ID:
                    self._sundaes_list.remove(i)
                
                
        total_P = price_drink + price_meal + price_side + price_sundaes
        order1 = order(order_ID, new_order_list, total_P)
        self._orders_list_unconfirmed.append(order1)
    
    def append_order(self, order_ID):
        for order in self._orders_list_unconfirmed:
            if order.ID == order_ID:
                self._orders_list.append(order)
                self._orders_list_unconfirmed.remove(order)
    
    def choose_combo(self, Combo_number, order_ID):
	        new_item_list = []
	        if self._inventory_system.combo_list[Combo_number] != None:
	            for i in self._inventory_system.combo_list[Combo_number].combo_elements:
	                item1 = self._inventory_system.search_item(i.name)
	                if i.num > item1.inventoryNum:
	                    print("error! {0} exceed the available amount! Please enter again.".format(item.name))   #check the meals inventory
	                    return None
	                new_item_list.append(i)       
	            meal = Meals(new_item_list,order_ID)   #check
	            self._meals_list.append(meal)
	        else:
	            return None              
        
    def update_status(self, order_ID):
        for order1 in self._orders_list:
            if order1.ID == order_ID:
                order1.update()
    #assert order.status == "available"
    
    def delete_list(self, order_ID):
        new_itemlll = []
        for i in self._sundaes_list:
            new_itemlll.append(i)
        for i in new_itemlll:
            if i.order_ID == order_ID:
                self._sundaes_list.remove(i)
        new_itemlll = []            
        for i in self._sides_list:
            new_itemlll.append(i)
        for i in new_itemlll:
            if i.order_ID == order_ID:
                self._sides_list.remove(i)
        new_itemlll = []            
        for i in self._drinks_list:
            new_itemlll.append(i)
        for i in new_itemlll:
            if i.order_ID == order_ID:
                self._drinks_list.remove(i)
        new_itemlll = []                       
        for i in self._meals_list:
            new_itemlll.append(i)
        for i in new_itemlll:
            if i.order_ID == order_ID:
                self._meals_list.remove(i)       
        new_itemlll = []                       
        for i in self._orders_list_unconfirmed:
            new_itemlll.append(i)
        for i in new_itemlll:
            self._orders_list_unconfirmed.remove(i)                                       
        new_itemlll = []
        for i in self._item_list:
            new_itemlll.append(i)
        for i in new_itemlll:
            if i.order_ID == order_ID:
                self._item_list.remove(i)
        
    def int_ordered(self, name, order_ID):
        for order in self._orders_list:
            if order.ID == order_ID:
                for item in order.meals[0].meal:    ##check
                    if item.name == name:
                        return item.num
                for i in range(1,len(order.meals) - 1):
                    if order.meals[i].name == name:
                        return order.meals[i].num
        return 0                       
                        
    def order_info(self, order_ID):
        for order in self._orders_list:
            if order.ID == order_ID:
                return order.status
        return "False ID"
        
            
    @property
    def order_ID(self):
        return len(self._orders_list)  #modify
    
             
    '''@property
    def order_ID(self):     #modify
        return self._order_ID     '''
        

    @property
    def orders_list(self):
        return self._orders_list
    
    @property
    def item_list(self):
        return self._item_list  # modify
    
    @property
    def meals_list(self):
        return self._meals_list        
                
    @property
    def drinks_list(self):
        return self._drinks_list
            
    @property
    def sides_list(self):
        return self._sides_list
        
    @property
    def inventory(self):
        return self._inventory_system


    @property 
    def sundaes_list(self):
        return self._sundaes_list
    

    @property
    def unconfirmed_list(self):  #modify
        return self._orders_list_unconfirmed

                    
    @property
    def combo_list(self):   #modify
        return self._combo_list
                      

    
    # change
    def set_meals_list(self, meals_list):
        self._meals_list = meals_list
