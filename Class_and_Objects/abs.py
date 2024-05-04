from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Concrete classes
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

# Function using abstraction
def print_area(shape):
    print("Area:", shape.area())

# Create instances of Rectangle and Circle
rectangle = Rectangle(5, 10)
circle = Circle(3)

# Call the function with different shapes
print_area(rectangle)  # Output: Area: 50
print_area(circle)     # Output: Area: 28.274333882308138
