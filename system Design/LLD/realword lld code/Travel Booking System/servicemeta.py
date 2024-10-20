class ServiceMeta(type):
    """
    Metaclass to automatically register each subclass of TravelService in a global registry.
    """
    registry = {}

    def __new__(cls, name, bases, dct):
        obj = super().__new__(cls, name, bases, dct)
        if name != 'TravelService':  
            cls.registry[name] = obj
        # print(cls.registry)
        return obj

    @classmethod
    def list_registered_services(cls):
        """List all registered services."""
        return list(cls.registry.keys())

    @classmethod
    def get_service_class(cls, service_name):
        """Get the class of a registered service by its name."""
        return cls.registry.get(service_name, None)

    @classmethod
    def remove_service(cls, service_name):
        """Remove a service class from the registry."""
        if service_name in cls.registry:
            del cls.registry[service_name]
            print(f"Service {service_name} removed from registry.")
        else:
            print(f"Service {service_name} not found in registry.")