class PriceDescriptor:
    """
    Descriptor class to manage and validate the price of travel services.
    Ensures prices are positive and within a reasonable range.
    """

    def __init__(self, name="price"):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Price must be positive!")
        instance.__dict__[self.name] = value