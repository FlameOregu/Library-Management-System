class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_borrowed = False

    def borrow(self):
        self.__is_borrowed = True

    def return_book(self):
        self.__is_borrowed = False

    def check_avb(self):
        if self.__is_borrowed == False:
            return True
        else:
            return False

    def display_info(self):
        print(self.title, self.author, self.__is_borrowed)

Book1 = Book("book1", "one")
Book2 = Book("book2", "two")
Book3 = Book("book3", "three")
Book4 = Book("book4", "four")
Book5 = Book("book5", "five")
Book6 = Book("book6", "six")

class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.check_avb() == True:
            self.borrowed_books.append(book)
            book.borrow()
        else:
            print("Dumb idiot the book is taken")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.pop(book)
            book.return_book()
        else:
            print("you dont have this book bro")

    def show_books(self):
        print(self.borrowed_books)

class PremiumUser(User):
    def __init__(self, name):
        User.__init__(self, name)
        self.borrow_limit = 5
    
    def borrow_book(self, book):
        if book.check_avb() == True and len(self.borrowed_books) < 5:
            self.borrowed_books.append(book)
            book.borrow()
        
        elif book.check_avb() == False:
            print("Book isn't available idiot")
        else:
            print("You have reached the maximum borrow limit")
User1 = User("User")
User2 = PremiumUser("PremiumUser")
