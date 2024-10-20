from hotelbooking import HotelBooking
from flightbooking import FlightBooking


class PackageDeal(HotelBooking, FlightBooking):
    """
    Class representing a package deal that combines both flight and hotel services.
    """

    def __init__(self, service_id, availibility, price, hotel_name, room_number, airline_name, flight_number):
        HotelBooking.__init__(self, service_id, availibility, price, hotel_name, room_number)
        FlightBooking.__init__(self, service_id, availibility, price, airline_name, flight_number)

    def calculate_cost(self):
        return (HotelBooking.calculate_cost(self) + FlightBooking.calculate_cost(self))