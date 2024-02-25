from Books import Book

class BookManager:
    #creates a new library file or reads already existing one
    def __init__(self, file_path="library.txt"):
        self.file_path = file_path
        self.load_books()

    def load_books(self):
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
                self.books = [Book(*line.strip().split(',')) for line in lines]
        except FileNotFoundError:
            self.books = []

    # wrties new books in the library file
    def save_books(self):
        with open(self.file_path, 'w') as file:
            for book in self.books:
                file.write(f"{book.title},{book.author},{book.year}\n")

    # Checks if entered books are already in the library and if not adds them
    def add_book(self, title, author, year):
        if not title or not author or not year.isdigit():
            print("Invalid input. Please provide valid information.")
            return

        existing_book = next((book for book in self.books if book.title.lower() == title.lower()), None)
        if existing_book:
            print(f"A book with the title '{title}' already exists.")
        else:
            new_book = Book(title, author, year)
            self.books.append(new_book)
            print(f"Book '{title}' added successfully.")
            self.save_books()

    # views all the books
    def view_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("\nList of Books:")
            for book in self.books:
                print(book)

    # searches book with the title
    def search_book(self, title):
        if not title:
            print("Invalid input. Please provide a valid title.")
            return

        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        if found_books:
            print(f"\nSearch results for '{title}':")
            for index, book in enumerate(found_books, start=1):
                print(f"{index}. Title: {book.title}, Author: {book.author}, Year: {book.year}")
        else:
            print(f"No books found with the title '{title}'.")