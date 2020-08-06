class Items():
    def __init__(self, name, num, order_ID):   
        self._name = name
        self._num = num
        self._order_ID = order_ID
        
    @property
    def name(self):
        return self._name
    
    @property
    def num(self):
        return self._num
    
    @property
    def order_ID(self):
        return self._order_ID
        
    
