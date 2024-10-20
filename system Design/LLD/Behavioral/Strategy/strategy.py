from abc import ABC, abstractmethod

# Strategy interface
class ShippingStrategy(ABC):
    @abstractmethod
    def calculate_shipping(self, order):
        pass

# Concrete Strategy for Standard Shipping
class StandardShipping(ShippingStrategy):
    def calculate_shipping(self, order):
        return 5.0  # flat rate for standard shipping

# Concrete Strategy for Express Shipping
class ExpressShipping(ShippingStrategy):
    def calculate_shipping(self, order):
        return 15.0  # flat rate for express shipping

# Concrete Strategy for Overnight Shipping
class OvernightShipping(ShippingStrategy):
    def calculate_shipping(self, order):
        return 25.0  # flat rate for overnight shipping

# Context class
class Order:
    def __init__(self, items, shipping_strategy: ShippingStrategy):
        self.items = items
        self.shipping_strategy = shipping_strategy

    def calculate_total(self):
        base_price = sum(item['price'] for item in self.items)
        shipping_cost = self.shipping_strategy.calculate_shipping(self)
        return base_price + shipping_cost

# Example usage
items = [
    {'name': 'Laptop', 'price': 1200},
    {'name': 'Mouse', 'price': 25}
]

# Choosing a shipping strategy
shipping_strategy = ExpressShipping()
order = Order(items, shipping_strategy)

print(f"Total order cost with express shipping: ${order.calculate_total()}")

# Switching strategy to Overnight Shipping
order.shipping_strategy = OvernightShipping()
print(f"Total order cost with overnight shipping: ${order.calculate_total()}")
