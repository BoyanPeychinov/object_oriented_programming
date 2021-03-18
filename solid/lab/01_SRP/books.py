class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0


class BookReaderStatus:
    def __init__(self, book):
        self.book = book
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self, books):
        self.books = books

    def add_book(self, book):
        self.books.append(book)


book_1 = Book("book1", "book1 author")
book_status_1 = BookReaderStatus(book_1)
book_status_2 = BookReaderStatus(book_1)