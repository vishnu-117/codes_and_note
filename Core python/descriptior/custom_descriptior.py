class PositiveNumber:

    def __get__(self, instance, owner):
        return instance._value
    
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("value must be positive")
        instance._value = value
    
    def __delete__(self, instance):
        del instance._value


class Product:

    price = PositiveNumber()

    def __init__(self, price):
        self.price = price


p = Product(50)
print(p.price)

try:
    p.price = -20
except ValueError as e:
    print(e)
