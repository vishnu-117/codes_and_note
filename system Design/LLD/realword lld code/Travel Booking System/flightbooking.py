from travelservice import AbstractTravelService


class FlightBooking(AbstractTravelService):
    """
    Class for representing a flight service. 
    Inherits from AbstractTravelService.
    """

    def __init__(self, service_id, availibility, price, airline_name, flight_number):
        AbstractTravelService.__init__(self, service_id, availibility, price)
        self.airline_name = airline_name
        self.flight_number = flight_number
    
    def calculate_cost(self):
        """
        Calculate the cost of the flight booking service,
        adding a 50% service charge.
        """
        return self.price * 1.5