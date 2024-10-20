from abc import ABC, abstractmethod


# Abstract Products
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(slef, amount):
        pass


class ShipmentOption(ABC):
    @abstractmethod
    def calculate_cost(self, weight):
        pass


# Concrete Products
class CreditCardPayment(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number
    
    def process_payment(self, amount):
        return f"Processing credit card payment  of Rs.{amount} using card {self.card_number}"


class PaypalPayment(PaymentMethod):
    def __init__(self, account_email):
        self.account_email = account_email
    
    def process_payment(self, amount):
        return f"Processing paypal payment of ${amount} using account {self.account_email}"


class StandardShipping(ShipmentOption):
    def __init__(self, destination):
        self.destination = destination
    
    def calculate_cost(self, weight):
        return f"Standrd shipping cost to {self.destination} for {weight} is Rs.{weight * 5}"


class ExpressShipping(ShipmentOption):
    def __init__(self, destionation):
        self.destination = destionation

    def calculate_cost(self, weight):
        return f"Express shipping cost to {self.destination} for {weight} is ${ weight * 10}"


# Abstract Factory:
class EcommerceFactory(ABC):
    @abstractmethod
    def create_payment_method(self, payment_details):
        pass

    @abstractmethod
    def create_shipping_options(self, shipping_details):
        pass


# Concrete Factories
class StandardEcommerceFactory(EcommerceFactory):
    def create_payment_method(self, payment_details):
        return CreditCardPayment(payment_details['card_number'])

    def create_shipping_options(self, shipping_details):
        return StandardShipping(shipping_details['destination'])


class ExpressEcommerceFactory(EcommerceFactory):
    def create_payment_method(self, payment_details):
        return PaypalPayment(payment_details['account_email'])

    def create_shipping_options(self, shipping_details):
        return ExpressShipping(shipping_details['destination'])

def process_order(factory: EcommerceFactory, amount, weight, payment_details, shipping_details):
    payment_method = factory.create_payment_method(payment_details)
    shipping_option = factory.create_shipping_options(shipping_details)

    paymet_result = payment_method.process_payment(amount)
    shipping_cost = shipping_option.calculate_cost(weight)

    print(paymet_result)
    print(shipping_cost)

#usage
print('Standard Ecommerce Order')
standard_factory = StandardEcommerceFactory()
payment_detaisl = {'card_number': '1234-5678-8765-4321'}
shipping_details = {'destination': 'New York'}
process_order(standard_factory, 100, 50, payment_detaisl, shipping_details)

print('Express Ecommerce Delivery')
express_factory = ExpressEcommerceFactory()
payment_detaisl = {'account_email': 'vishnu@amazon.com'}
shipping_details = {'destination': 'Pune'}
process_order(express_factory, 200, 100, payment_detaisl, shipping_details)