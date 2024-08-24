class Library:
    def __init__(self, books):
        self.available_books = books
    
    def display_available_books(self):
        for book in self.available_books:
            print("Name: ",book)
    
    def lend_book(self, book_search):
        if self.book_search in self.available_books:
            print(f"You borrowed ___{self.book_search}___")
            self.available_books.remove(book_search)
        else:
            print("Book is not Available!!!!!....")
    def add_books(self):
        pass
    
class Customer:
    def request_book(self):
        print("Enter the Book You Want: ")
        self.book_search = input()
        return self.book
    
    def return_book(self):
        print("Enter the name of the Book You Returning: ")
        book_return = input()
        return self.book_return
    
library = Library(["Ikigai", "Atomic Habits", "You Can", "Secret"])
library.display_available_books()

customer = Customer()

