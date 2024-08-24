class Library:
    def __init__(self, books):
        self.available_books = books
    
    def display_available_books(self):
        for book in self.available_books:
            print("Name: ",book)
    
    def lend_book(self, book_search):
        if book_search in self.available_books:
            print(f"You borrowed ___{self.book_search}___")
            self.available_books.remove(book_search)
        else:
            print("Book is not Available!!!!!....")
            
    def add_books(self,return_book):
        self.available_books.append(return_book)
        print(f"You have returned {return_book}. Thank You...")
    
class Customer:
    def request_book(self):
        print("Enter the Book You Want: ")
        self.book = input()
        return self.book
    
    def return_book(self):
        print("Enter the name of the Book You Returning: ")
        self.book = input()
        return self.book
    
library = Library(["Ikigai", "Atomic Habits", "You Can", "Secret"])
library.display_available_books()

customer = Customer()
while True:
    print("1. Display \n2. Request a Book \n3. Return a Book\n4. Exit")
    user_choice = int(input())
    if user_choice == 1:
        library.display_available_books()
    elif user_choice == 2:
        requested_book = customer.request_book()
        library.lend_book(requested_book)
    elif user_choice == 3:
        return_book = customer.return_book()
        library.add_books(return_book)
    elif user_choice == 4:
        quit()
    else:
        print("You entered a Wrong command")
        quit()

