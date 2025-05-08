from library_system import LibrarySystem


def main_menu(library):
    while True:
        print("\n===== LIBRARY SYSTEM MENU =====")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Show All Books")
        print("6. Show Borrowed Books")
        print("7. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Book title: ")
            author = input("Author: ")
            library.add_book(title, author)

        elif choice == "2":
            name = input("Member name: ")
            library.add_member(name)

        elif choice == "3":
            name = input("Member name: ")
            title = input("Book title: ")
            library.borrow_book(name, title)

        elif choice == "4":
            name = input("Member name: ")
            title = input("Book title: ")
            library.return_book(name, title)

        elif choice == "5":
            library.show_all_books()

        elif choice == "6":
            library.show_borrowed_books()

        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")