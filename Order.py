from meals import Meals
from inventory_system import Inventory_system

I_s = Inventory_system()

class order():
    
    def __init__(self, order_ID, meals, price):
        self._meals = meals
        self._status = "invalid"
        self._order_ID = order_ID
        self._price = price

    
    def update(self):
        self._status = "available"
    
    @property
    def price(self):
        return self._price
        
    @property
    def status(self):
        return self._status

    @property
    def ID(self):
        return self._order_ID

    @property
    def meals(self):
        return self._meals
