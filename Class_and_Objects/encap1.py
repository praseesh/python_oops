class Car:
    def __init__(self, make, model, mileage):
        self.__make = make  # private attribute
        self.__model = model  # private attribute
        self.__mileage = mileage  # private attribute

    def get_make(self):  # getter method
        return self.__make

    def set_make(self, make):  # setter method
        self.__make = make

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_mileage(self):
        return self.__mileage

    def set_mileage(self, mileage):
        if mileage >= 0:
            self.__mileage = mileage
        else:
            raise ValueError("Mileage cannot be negative")

# Creating an instance of Car
my_car = Car("Toyota", "Corolla", 50000)

# Accessing and modifying private attributes using getter and setter methods
print("Make:", my_car.get_make())  # Output: Make: Toyota
print("Model:", my_car.get_model())  # Output: Model: Corolla
print("Mileage:", my_car.get_mileage())  # Output: Mileage: 50000

my_car.set_mileage(60000)
print("Updated Mileage:", my_car.get_mileage())  # Output: Updated Mileage: 60000

# Trying to set a negative mileage
try:
    my_car.set_mileage(-1000)
except ValueError as e:
    print(e)  # Output: Mileage cannot be negative
