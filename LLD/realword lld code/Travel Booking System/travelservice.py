from abc import ABC, abstractmethod, ABCMeta
from servicemeta import ServiceMeta


class CombinedMeta(ABCMeta, ServiceMeta):
    """
    Combined metaclass that merges ABCMeta (for abstract base classes) and ServiceMeta
    (for automatic registration of subclasses).
    """
    pass


class AbstractTravelService(ABC, metaclass=CombinedMeta):
    """
    Abstract base class for all travel services, using ServiceMeta as its metaclass.
    Implements common attributes and methods, such as managing service details and calculating costs.
    """

    total_services = 0

    def __init__(self, service_id, availability, price):
        self.__service_id = service_id
        self.__availability = availability
        self.__price = price
        AbstractTravelService.total_services = 2
    
    @property
    def service_id(self):
        return self.__service_id
    
    @property
    def availability(self):
        return self.__availability
    
    @availability.setter
    def availability(self, value):
        self.__availability = value
    
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @abstractmethod
    def calculate_cost(self):
        pass

    @classmethod
    def get_total_services(cls):
        return cls.total_services

    @staticmethod
    def is_valid_service_id(service_id):
        return isinstance(service_id, str) and (service_id.startswith('HB') or service_id.startswith('FB') or service_id.startswith('PD'))

    def __str__(self):
        return f"Service id: {self.__service_id}, Availability: {self.__availability}, Price: {self.__price}"

    def __repr__(self):
        return f"Travel service: {self.__service_id},{self.__availability}, {self.__price}"

    def __eq__(self, value):
        return self.__price == value