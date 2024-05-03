class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Car(Vehicle):
    def drive(self):
        return f"{self.brand} {self.model} is driving on the road."

class Motorcycle(Vehicle):
    def drive(self):
        return f"{self.brand} {self.model} is driving on the highway."

class Truck(Vehicle):
    def drive(self):
        return f"{self.brand} {self.model} is driving on the highway carrying cargo."

# Polymorphic function
def drive_vehicle(vehicle):
    print(vehicle.drive())

# Create instances of Car, Motorcycle, and Truck
car = Car("Toyota", "Camry")
motorcycle = Motorcycle("Honda", "CBR600RR")
truck = Truck("Ford", "F-150")

# Call the function with different instances
drive_vehicle(car)         # Output: Toyota Camry is driving on the road.
drive_vehicle(motorcycle)  # Output: Honda CBR600RR is driving on the highway.
drive_vehicle(truck)       # Output: Ford F-150 is driving on the highway carrying cargo.
