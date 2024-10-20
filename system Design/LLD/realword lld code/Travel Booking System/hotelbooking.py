from travelservice import AbstractTravelService


class HotelBooking(AbstractTravelService):
    """
    Class representing a hotel booking service. 
    Inherits from AbstractTravelService.
    """

    def __init__(self, service_id, availibility, price, hotel_name, room_number):
        AbstractTravelService.__init__(self, service_id, availibility, price)
        self.hotel_name = hotel_name
        self.room_number = room_number
    
    def calculate_cost(self):
        """
        Calculate the cost of the hotel service,
        adding a 30% service charge.
        """
        return self.price * 1.3