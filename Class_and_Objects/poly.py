import math

class Shape:
    def area(self):
        pass

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
        return math.pi * self.radius ** 2

# Function to calculate the total area of shapes
def total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return total

# Create instances of Rectangle and Circle
shapes = [Rectangle(5, 10), Circle(3)]

# Calculate and print total area
print("Total area:", total_area(shapes))  # Output: Total area: 104.71238898038469
