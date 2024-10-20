import random

class Car:
    def __init__(self):
        self.generator = random.Random()

    def accelerate(self):
        random_num = self.generator.randint(50, 100)
        speed = random_num
        print(f"The speed of the car is {speed} mph")

    def apply_brakes(self):
        random_num = self.generator.randint(20, 40)
        speed = random_num
        print(f"The speed of the car is {speed} mph after applying the brakes")

    def assign_driver(self, driver_name):
        print(f"{driver_name} is driving the car")

class Motorcycle:
    def __init__(self):
        self.generator = random.Random()

    def rev_throttle(self):
        random_num = self.generator.randint(50, 100)
        speed = random_num
        print(f"The speed of the motorcycle is {speed} mph")

    def pull_brake_lever(self):
        random_num = self.generator.randint(20, 40)
        speed = random_num
        print(
            f"The speed of the motorcycle is {speed} mph after applying the brakes")

    def assign_rider(self, rider_name):
        print(f"{rider_name} is riding the motorcycle")  

import traceback

if __name__ == '__main__':
    car = Car()
    bike = Motorcycle()

    print("The Motorcycle\n")
    bike.assign_rider("Subodh")
    bike.rev_throttle()
    bike.pull_brake_lever()
    print("\n")

    print("The Car\n")
    car.assign_driver("Sushant")
    car.accelerate()
    car.apply_brakes()
    print("\n")

    print("Attempting to call client methods with the service object\n")

    try:
        bike.assign_driver("Robert")
        bike.accelerate()
        bike.apply_brakes()
    except AttributeError:
        print("Oops! bike object cannot access car methods")
        traceback.print_exc()

