class Library:
    def __init__(self, books):
        self.available_books = books
    
    def display_available_books(self):
        for book in self.available_books:
            print("Name: ",book)
    
    def lend_book(self):
        pass
    
    def add_books(self):
        pass
    
class Customer:
    def request_book(self):
        pass
    
    def return_book(self):
        pass
    
library = Library(["Ikigai", "Atomic Habits", "You Can", "Secret"])
library.display_available_books()

