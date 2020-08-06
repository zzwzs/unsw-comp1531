from inventory_system import Inventory_system

I_s = Inventory_system()

class Meals():
    def __init__(self, meal, order_ID):#patties, buns, ingredient, sides, drinks, ):
        self._order_ID = order_ID
        self._meal = meal
        
        
    def calc(self, item1):
        item2 = I_s.search_item(item1.name)
        return int(item1.num) * int(item2.price)

    @property
    def order_ID(self):
        return self._order_ID

    @property
    def meal(self):
        return self._meal
