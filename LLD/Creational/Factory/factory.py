from abc import ABC, abstractmethod

# Product:
class Ticket(ABC):
    @abstractmethod
    def get_details(self):
        pass

# Concrete Products:
class StandardTicket(Ticket):
    def __init__(self, seat_number):
        self.seat_number = seat_number
    
    def get_details(self):
        return f"Standard ticket for seat no {self.seat_number}"


class PremiumTicket(Ticket):
    def __init__(self, seat_number):
        self.seat_number = seat_number

    def get_details(self):
        return f"Premium Ticket for seat {self.seat_number}"


class VIPTicket(Ticket):
    def __init__(self, seat_number):
        self.seat_number = seat_number

    def get_details(self):
        return f"VIP Ticket for seat {self.seat_number}"


class TicketFactory:

    @staticmethod
    def create_ticket(seat_number, ticket_type):
        if ticket_type == 'Standard':
            return StandardTicket(seat_number)
        elif ticket_type == 'Premium':
            return PremiumTicket(seat_number)
        elif ticket_type == 'VIP':
            return VIPTicket(seat_number)
        else:
            raise ValueError(f"Unknown ticket type: {ticket_type}")

def book_ticket(seat_number, ticket_type):
    ticket = TicketFactory.create_ticket(seat_number, ticket_type)
    print(ticket.get_details())

#Usage
book_ticket(117, 'VIP')
book_ticket(58, 'Standard')
book_ticket(17, 'Premium')
