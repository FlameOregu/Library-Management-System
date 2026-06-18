class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_borrowed = False

    def borrow(self):
        self.__is_borrowed = True

    def return_book(self):
        self.__is_borrowed = False

    def is_available(self):
        return not self.__is_borrowed

    def display_info(self):
        status = "Available" if self.is_available() else "Borrowed"
        print(f"'{self.title}' by {self.author} — {status}")


class User:
    BORROW_LIMIT = 3

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_available():
            print(f"'{book.title}' is not available.")
        elif len(self.borrowed_books) >= self.BORROW_LIMIT:
            print(f"{self.name} has reached the borrow limit ({self.BORROW_LIMIT} books).")
        else:
            self.borrowed_books.append(book)
            book.borrow()
            print(f"{self.name} borrowed '{book.title}'.")

    def return_book(self, book):
        if book not in self.borrowed_books:
            print(f"{self.name} does not have '{book.title}'.")
        else:
            self.borrowed_books.remove(book)  # fix: was pop(book)
            book.return_book()
            print(f"{self.name} returned '{book.title}'.")

    def show_books(self):
        if not self.borrowed_books:
            print(f"{self.name} has no borrowed books.")
        else:
            titles = ", ".join(f"'{b.title}'" for b in self.borrowed_books)
            print(f"{self.name}'s borrowed books: {titles}")


class PremiumUser(User):
    BORROW_LIMIT = 10

    def __init__(self, name):
        super().__init__(name)  # fix: was User.__init__(self, name)
