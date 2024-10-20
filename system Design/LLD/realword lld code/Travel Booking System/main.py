from decorators import log_details, validate_booking
from flightbooking import FlightBooking
from hotelbooking import HotelBooking
from packagedeal import PackageDeal
from bookingcontext import BookingContext


@log_details
@validate_booking
def book_service(service):
    """
    Function to book a travel service.
    Uses decorators to log interaction and validate booking details.
    """
    print(f"Booking service: {service}")
    return f"Successfully booked {service}"


def display_services(services):
    """
    Function to display a list of services for user selection.
    """
    for idx, service in enumerate(services):
        print(f"{idx}. {service}")

def select_service(services, service_type):
    """
    Function to allow user to select a specific service type to book.
    Handles user input and validation.
    """
    print(f"\nSelect a {service_type} to book:")
    display_services(services)
    choice = int(input(f"Enter the number corresponding to the {service_type} you want to book: "))
    if 0 <= choice < len(services):
        return services[choice]
    else:
        print("Invalid choice. Please try again.")
        return select_service(services, service_type)

if __name__ == "__main__":
    flights = [
        FlightBooking("FB001", 10, 500, "Airline A", "AA101"),
        FlightBooking("FB002", 5, 700, "Airline B", "BB202"),
        FlightBooking("FB003", 8, 600, "Airline C", "CC303")
    ]

    hotels = [
        HotelBooking("HB004", 3, 300, "HotelBooking A", "100"),
        HotelBooking("HB005", 2, 450, "HotelBooking B", "102"),
        HotelBooking("HB006", 4, 200, "HotelBooking C", "103")
    ]

    package_deals = [
        PackageDeal("PD007", 2, 1000, "HotelBooking D", "100", "Airline D", "DD404"),
        PackageDeal("PD008", 1, 1200, "HotelBooking E", "101", "Airline E", "EE505"),
        PackageDeal("PD009", 3, 800, "HotelBooking F", "102", "Airline F", "FF606")
    ]

    print("Welcome to the Travel Booking System!")
    print("Options: \n1. Book a FlightBooking\n2. Book a HotelBooking\n3. Book a Package Deal")

    option = input("Please select an option (1-3): ")

    try:
        if option == '1':
            selected_service = select_service(flights, "FlightBooking")
        elif option == '2':
            selected_service = select_service(hotels, "HotelBooking")
        elif option == '3':
            selected_service = select_service(package_deals, "Package Deal")
        else:
            print("Invalid option selected. Exiting the booking system.")
            exit()

        with BookingContext():
            try:
                print(book_service(selected_service))
            except ValueError as e:
                print(e)
    except Exception as e:
        print(f"An error occurred: {e}")
