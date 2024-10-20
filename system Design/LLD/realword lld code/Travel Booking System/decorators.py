from travelservice import AbstractTravelService
from functools import wraps

def log_details(func):
    """
    Decorator to log bookings details
    Prints log information before and after the function call.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Booking attempt for function {func.__name__} with parameter {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Booking result {result}")
        return result

    return wrapper

def validate_booking(func):
    """
    Decorator for validating booking
    Ensures service availability and price are valid before booking.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        instance = args[0]
        if isinstance(instance, AbstractTravelService):
            if instance.availability == 0:
                raise ValueError("Service is unavailable, you can't do booking....")
            elif instance.price < 0:
                raise ValueError("Booking price must be grater than zero....")
            print("[VALIDATED] Booking details are valid.")
        return func(*args, **kwargs)
    return wrapper