class Product:

    def __init__(self, price):
        self._price = price
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Price must be positive')
        self._price = value
    
    @price.deleter
    def price(self):
        del self._price

p = Product(50)
print(p.price)

try:
    p.price = -1
except Exception as e:
    print(e)