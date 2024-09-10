from ABC import ABC, abstract method the 
import copy

# Abstract Class
class Vehicle(ABC):
    # Constructor:
    def __init__(self,seats, tyres, color, fuel):
        self.seats = seats
        self.tyres = tyres
        self.color = color
        self.fuel = fuel

    # Clone Method:
    @abstractmethod
    def clone(self):
        pass
    
    # Printing objects as per our requirement:
    def __str__(self):
        return f"Seats = {self.seats}\nTyres = {self.tyres}\nColor = {self.color}\nFuel = {self.fuel}"

# First Child class:
class Bike(Vehicle):
    
    # Constructor:
    def __init__(self, seats, tyres, color, fuel):
        super().__init__(seats, tyres, color, fuel)

    # Overwritting Cloning Method:
    def clone(self):
        return copy.deepcopy(self)

# Second Child class:        
class Car(Vehicle):
    
    # Constructor:
    def __init__(self, seats, tyres, color, fuel):
        super().__init__(seats, tyres, color, fuel)

    # Overwritting Cloning Method:
    def clone(self):
        return copy.deepcopy(self)

# main() method       
def main():
    vehicles = [] # List for Original objects
    vehiclesCopy = [] # List of Prototyped objects
    
    b1 = Bike(1,2, 'Black', 'Petrol') # Creating Bike object
    c1 = Car(5,4, 'White', 'Electric') # Creating Car object
    
    vehicles.append(b1) # Adding Bike object into the List
    vehicles.append(c1) # Adding Car object into the List
    
    b1Copy = b1.clone() # Clonning Bike object
    c1Copy = c1.clone() # Clonning Car object
    
    vehiclesCopy.append(b1Copy) # Adding Clonned Bike object into the List
    vehiclesCopy.append(c1Copy) # Adding Clonned Car object into the List
    
    print("Original Objects:")
    for v in vehicles:# Printing Original Objects
        print(v)
        print("---------------------------------------------------")
    print("\n\n\nPrototyped Objects:")
    for vC in vehiclesCopy: # Printing Prototypes Objects
        print(vC)
        print("---------------------------------------------------")
    
if __name__=="__main__":
    main()
