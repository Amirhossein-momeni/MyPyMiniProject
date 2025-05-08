from book import Book
from member import Member


class LibrarySystem:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book '{title}' by {author} added successfully.")

    def add_member(self, name):
        if any(m.name == name for m in self.members):
            print("Member already exists!")
        else:
            new_member = Member(name)
            self.members.append(new_member)
            print(f"Member '{name}' added successfully.")

    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if not member:
            print("Member not found.")
        elif not book:
            print("Book not found.")
        else:
            member.borrow_book(book)

    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if not member or not book:
            print("Invalid member or book.")
        else:
            member.return_book(book)

    def show_all_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("\nAll Books:")
            for b in self.books:
                status = "Borrowed" if b.is_borrowed else "Available"
                print(f"- {b.title} by {b.author} [{status}]")

    def show_borrowed_books(self):
        print("\nBorrowed Books:")
        any_borrowed = False
        for member in self.members:
            if member.borrowed_books:
                any_borrowed = True
                print(f"\n- {member.name}:")
                for book in member.borrowed_books:
                    print(f"   * {book.title} by {book.author}")
        if not any_borrowed:
            print("No borrowed books.")