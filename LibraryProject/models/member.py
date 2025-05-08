class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_borrowed:
            print(f"The book '{book.title}' is already borrowed.")
        else:
            book.is_borrowed = True
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} has not borrowed '{book.title}'")