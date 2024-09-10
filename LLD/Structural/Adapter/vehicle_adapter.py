# Existing vehicle management system

class Vehicle:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def get_license_plate(self):
        return self.license_plate


class ParkingLot:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def get_vehicles(self):
        return self.vehicles


# External electric vehicle system with a different interface

class ElectricVehicle:
    def __init__(self, id):
        self.id = id

    def get_id(self):
        return self.id


# Adapter to make ElectricVehicle compatible with the ParkingLot

class ElectricVehicleAdapter(Vehicle):
    def __init__(self, electric_vehicle):
        self.electric_vehicle = electric_vehicle

    def get_license_plate(self):
        # Assume electric vehicle ID can be used as a license plate
        return self.electric_vehicle.get_id()


# Usage

# Existing parking lot system
parking_lot = ParkingLot()

# Adding a regular vehicle
vehicle = Vehicle("ABC123")
parking_lot.add_vehicle(vehicle)

# External electric vehicle system
electric_vehicle = ElectricVehicle("EV456")

# Using adapter to add electric vehicle to the parking lot
electric_vehicle_adapter = ElectricVehicleAdapter(electric_vehicle)
parking_lot.add_vehicle(electric_vehicle_adapter)

# Display vehicles in the parking lot
for vehicle in parking_lot.get_vehicles():
    print(f"License Plate: {vehicle.get_license_plate()}")
