# library.py
from book import Book

class Library:
    _instance = None  # Singleton instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Library, cls).__new__(cls)
            cls._instance.books = []
        return cls._instance

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book '{title}' added successfully!")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nLibrary Collection:")
            for index, book in enumerate(self.books, start=1):
                print(f"{index}. {book}")

    def search_book(self, search_term):
        search_term = search_term.lower()
        found_books = [book for book in self.books if search_term in book.title.lower() or search_term in book.author.lower()]
        if found_books:
            print("\nSearch Results:")
            for index, book in enumerate(found_books, start=1):
                print(f"{index}. {book}")
        else:
            print("No books found matching your search criteria.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    book.available = False
                    print(f"You have successfully borrowed '{book.title}'.")
                    return
                else:
                    print(f"Sorry, '{book.title}' is currently borrowed.")
                    return
        print("Book not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.available:
                    book.available = True
                    print(f"Thank you for returning '{book.title}'.")
                    return
                else:
                    print(f"'{book.title}' is already marked as available.")
                    return
        print("Book not found in the library.")