

class Book:
    def __init__(self) :

        self.name = name
        self.author = author
        print(f"{self.name} is written by {self.author}")
        
    def info(self):
        print(f"{name} is written by {author}")
# book1 = Book("The Da Vinci Code", "Dan Brown")
name = "Cosmos"
author = "Carl Sagan"
book2 = Book()
book2.info()


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def display(self):
        print(f"Car make: {self.make}, model: {self.model}")
