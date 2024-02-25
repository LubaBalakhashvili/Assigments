from BookManager import BookManager


book_manager = BookManager()

while True:
    #let users choose actions they want to do with library

    print("\nMenu:")
    print("1. Add a new book")
    print("2. View all books")
    print("3. Search for a book")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    #depending on choice functions are called from book manager class
    if choice == '1':
        print("\nEnter details for the new book:")
        title = input("Title: ")
        author = input("Author: ")
        year = input("Year of publication: ")
        book_manager.add_book(title, author, year)

    elif choice == '2':
        book_manager.view_books()

    elif choice == '3':
        search_title = input("\nEnter the title to search for: ")
        book_manager.search_book(search_title)

    elif choice == '4':
        print("\nExiting the application. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please enter a valid option.")

