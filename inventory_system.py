from Inventory import inventory
from items import Items
from combo import Combo
from combos import Combos

class Inventory_system():

    def __init__(self):
        self._buns_list = []
        self._patties_list = []
        self._ingredient_list = []
        self._sides_list = []
        self._drinks_list = []
        self._sundaes_list = []
        self._combo_list = []
        self._combo_elements = []
        
        
      
      
    def add_buns(self, buns):
        self._buns_list.append(buns)
        
    def add_patties(self, patties):
        self._patties_list.append(patties)
                  
    def add_ingredient(self, ingredient):
        self._ingredient_list.append(ingredient)
        
    def add_sides(self, sides):
        self._sides_list.append(sides)
    
    def add_drinks(self, drinks):
        self._drinks_list.append(drinks)
        
    def add_sundaes(self, sundaes):
        self._sundaes_list.append(sundaes)
        
    def search_item(self, name):
        
        for buns in self._buns_list:
            if buns.itemName == name:
                return buns
        
        for patties in self._patties_list:
            if patties.itemName == name:
                return patties
        
        for ingredients in self._ingredient_list:
            if ingredients.itemName == name:
                return ingredients
                
        for sides in self._sides_list:
            if sides.itemName == name:
                return sides
                
        for drinks in self._drinks_list:
            if drinks.itemName == name:
                return drinks
                
        for sundaes in self._sundaes_list:
            if sundaes.itemName == name:
                return sundaes
                
        return None
    
     #New Features
            
    def make_a_combo(self, name, num):
        #price = 0
        #inven_element = self._buns_list[0]
        
        for buns in self._buns_list:
            if buns.itemName == name:
                inven_element = buns
        
        for patties in self._patties_list:
            if patties.itemName == name:
                inven_element = patties
        
        for ingredients in self._ingredient_list:
            if ingredients.itemName == name:
                inven_element = ingredients
                
        for sides in self._sides_list:
            if sides.itemName == name:
                inven_element = sides
                
        for drinks in self._drinks_list:
            if drinks.itemName == name:
                inven_element = drinks
                
        for sundaes in self._sundaes_list:
            if sundaes.itemName == name:
                inven_element = sundaes
                
        if num > inven_element.inventoryNum:
            print("error! {0} exceed the available amount! Please enter again.".format(name))   #check the inventory
            return None
        price = inven_element.itemPrice * num
        Element = Combo(name, num, price)
        self._combo_elements.append(Element)
    
    @property    
    def make_combo_list(self):
        total_Price = 0
        for element in self._combo_elements:
            total_Price = total_Price + element.price
        No = str(len(self.combo_list) + 1)
        combo = Combos(self._combo_elements, total_Price, No)
        self._combo_list.append(combo)
        self._combo_elements = []

        
        
    @property
    def buns_list(self):
        return self._buns_list
    
    @property
    def patties_list(self):
        return self._patties_list
            
    @property
    def ingredient_list(self):
        return self._ingredient_list
    
    @property
    def sides_list(self):
        return self._sides_list
    
    @property
    def drinks_list(self):
        return self._drinks_list 
        
    @property
    def sundaes_list(self):
        return self._sundaes_list 
        
    @property
    def combo_list(self):
        return self._combo_list   
    @property
    def combo_elements(self):
        return self._combo_elements
    
    
             
