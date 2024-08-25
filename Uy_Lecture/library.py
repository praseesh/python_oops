class Library:
    def __init__(self, books):
        self.available_books = books
    
    def display_available_books(self):
        print("Available Books:")
        for book in self.available_books:
            print("Name:", book)
    
    def lend_book(self, book_search):
        if book_search in self.available_books:
            print(f"You borrowed '{book_search}'")
            self.available_books.remove(book_search)
        else:
            print("Book is not available!!!!!....")
    
    def add_books(self, return_book):
        self.available_books.append(return_book)
        print(f"You have returned '{return_book}'. Thank you!")
    
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
    print("\n1. Display available books \n2. Request a Book \n3. Return a Book\n4. Exit")
    user_choice = int(input("Choose an option: "))
    if user_choice == 1:
        library.display_available_books()
    elif user_choice == 2:
        requested_book = customer.request_book()
        library.lend_book(requested_book)
    elif user_choice == 3:
        return_book = customer.return_book()
        library.add_books(return_book)
    elif user_choice == 4:
        print("Exiting the system. Goodbye!")
        break
    else:
        print("You entered a wrong command. Exiting...")
        break
