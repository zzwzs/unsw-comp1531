
class Combo():
    
    def __init__(self, name, num, price):
        #self._elements = elements
        self._price = price
        self._name = name
        self._num = num

    
            
    '''@property
    def elements(self):
        return self._elements
    '''    
    @property
    def price(self):
        return self._price
    
    @property
    def name(self):
        return self._name
        
    @property
    def num(self):
        return self._num
    
