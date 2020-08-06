#from abc import ABC

class inventory():

    def __init__(self, itemPrice, itemName, inventoryNum):
        self._itemPrice = itemPrice
        self._itemName = itemName
        self._inventoryNum = inventoryNum
        #self._combo_list = []
    
    
    @property
    def itemName(self):
        return self._itemName

    @property
    def itemPrice(self):
        return self._itemPrice

    @property
    def inventoryNum(self):
        return self._inventoryNum
    
    def add_inventory(self, edit):
        self._inventoryNum = self._inventoryNum + edit
    
    def used_inventory(self, edit):
        self._inventoryNum = self._inventoryNum - edit
    
        
    def calc_price(self, num):
        return num * itemPrice
        
    def __str__(self):
        return "this is inventory"
        
        
class buns(inventory):
    def __init__(self, price, name, num):
        super().__init__(price, name, num)
    
class patties(inventory):
    def __init__(self, price, name, num):
        super().__init__(price, name, num)
    
class sides(inventory):
    def __init__(self, price, name, num):
        super().__init__(price, name, num)
    
class drinks(inventory):
    def __init__(self, price, name, num):
        super().__init__(price, name, num)
    
class ingredient(inventory):
    def __init__(self, price, name, num):
        super().__init__(price, name, num)
    
class Sundaes(inventory):
    def __init__(self, price, name, num):
        super().__init__(price, name, num)
