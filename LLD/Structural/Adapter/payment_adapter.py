from abc import ABC, abstractmethod

# Unified Payment Processor Interface
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount, currency, payment_method):
        pass


# Payment Gateway A
class PaymentGatewayA:
    def make_payment(self, amount, currency_code, method):
        print(f"PaymentGatewayA processing payment: {amount} {currency_code} via {method}")


# Payment Gateway B
class PaymentGatewayB:
    def execute_transaction(self, value, currency_type, mode):
        print(f"PaymentGatewayB executing transaction: {value} {currency_type} with {mode}")


# Adapter for PaymentGatewayA
class PaymentGatewayAAdapter(PaymentProcessor):
    def __init__(self, gateway_a):
        self.gateway_a = gateway_a

    def process_payment(self, amount, currency, payment_method):
        self.gateway_a.make_payment(amount, currency, payment_method)


# Adapter for PaymentGatewayB
class PaymentGatewayBAdapter(PaymentProcessor):
    def __init__(self, gateway_b):
        self.gateway_b = gateway_b

    def process_payment(self, amount, currency, payment_method):
        self.gateway_b.execute_transaction(amount, currency, payment_method)


# Unified payment system
def process_payment(payment_processor, amount, currency, payment_method):
    payment_processor.process_payment(amount, currency, payment_method)

# Create instances of payment gateways
gateway_a = PaymentGatewayA()
gateway_b = PaymentGatewayB()

# Create adapters for these gateways
adapter_a = PaymentGatewayAAdapter(gateway_a)
adapter_b = PaymentGatewayBAdapter(gateway_b)

# Process payments using the unified interface
process_payment(adapter_a, 100, 'USD', 'credit_card')
process_payment(adapter_b, 200, 'EUR', 'debit_card')
