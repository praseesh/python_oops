class Car:
    no_of_wheels = 4
    _year_of_manufacture = 2017
    __color = "black"
    def __init__(self):
        print(f"Protected Attributes color is : {self.__color}\nYear:{self._year_of_manufacture}")
        print(f"Protected Attribute year is: {self._year_of_manufacture}")
        
    def change_color(self,color):
        self.__color=color
    def display_color(self):
        print(f"New color: {self.__color}")
        
class Audi(Car):
    def __init__(self):
        print(f"Protected Attributes color is : \nYear:{self._year_of_manufacture}")

car = Car()   
print(f"Protected Attributes color is : \nYear:{car._year_of_manufacture}")
car.display_color()
car.change_color("Green")
car.display_color()
audi = Audi()
# print(f"Protected Attributes color is :{audi._Car__color} \nYear:{audi._year_of_manufacture}")

    
    
    
    
    