from inventory_system import Inventory_system

I_s = Inventory_system()

class Mains():
    def __init__(self, meal, order_ID):#patties, buns, ingredient, sides, drinks, ):
        '''self._patties = {}
        self._buns = {}
        self._ingredient = {}
        self._sides = {}
        self._drinks = {}'''
        self._order_ID = order_ID
        self._meal = meal
        
    '''
    @property
    def patties_num(self):
        return self._patties_num

    @property
    def buns_num(self):
        return self._buns_num

    @property
    def ingredient_num(self):
        return self._ingredient_num

    @property
    def sides_num(self):
        return self._sides_num
    
    @property
    def drinks_num(self):
        return self._drinks_num
    '''
        
    def calc(self):
        tot_p = 0
        Item = I_s.search_item(Items.name)
        if Item != None:
            for item in Items.ordered:
                tot_p = tot_p + Items.ordered[item] * Item.price
    
        return tot_p
        '''price_b = 0
        price_i = 0
        price_p = 0
        price_s = 0
        price_d = 0
        for char in patties:
            price_p = price_p + meals.patties[char] * I_s.char._price             #patties[char] is the number of patties customer want to buy
        for char in buns:
            price_b = price_b + meals.buns[char] * I_s.char._price
        for char in ingredient:
            price_i = price_i + meals.ingredient[char] * I_s.char._price
        for char in sides:
            price_i = price_i + meals.sides[char] * I_s.char._price
        for char in drinks:
            price_i = price_i + meals.drinks[char] * I_s.char._price
        tot_p = price_b + price_d + price_i + price_p + price_s
        return tot_p'''
        
        

