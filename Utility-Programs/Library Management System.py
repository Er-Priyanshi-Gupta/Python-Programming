class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []
    def check(self):
        if (self.no_of_books != len(self.books)):
            return 0
        else:
            return 1
    def addBooks(self,book):
        self.books.append(book)
        self.no_of_books = len(self.books)
        
    def removeBook(self,book):
        self.books.remove(book)
        self.no_of_books = len(self.books)
    
    def show(self):
        print(f"The library has {self.no_of_books} books. The books are")
        for book in self.books: print(book)
        
library1 = Library()
library1.addBooks(input("Enter book\n"))
# library1.addBooks(input("Enter book\n"))
# library1.addBooks(input("Enter book\n"))
# library1.addBooks(input("Enter book\n"))
# library1.addBooks(input("Enter book\n"))
# library1.addBooks(input("Enter book\n"))
# library1.addBooks(input("Enter book\n"))
# library1.addBooks(input("Enter book\n"))
# library1.addBooks(input("Enter book\n"))
# library1.addBooks(input("Enter book\n"))
library1.show()