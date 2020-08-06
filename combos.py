
class Combos():
    def __init__(self,combo_elements, price, No):#patties, buns, ingredient, sides, drinks, ):
        self._price = price
        self._combo_elements = combo_elements
        self._combo_No = No
    
    @property
    def price(self):
        return self._price

    @property
    def combo_elements(self):
        return self._combo_elements

    @property
    def No(self):
        return self._combo_No
