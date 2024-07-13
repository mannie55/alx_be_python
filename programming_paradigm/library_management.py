class Book:
        def __init__(self, title, author):
            self.title = title
            self.author = author
            self._is_checked_out = False
        def checkout(self):
            # if not self._is_checked_out:
            self._is_checked_out = True
            return True
            return False

        def return_book(self):
            # if self._is_checked_out:
            self._is_checked_out = False
            return True
            return False
    
class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.checkout():
                    return title
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return title
        return False

    def list_available_books(self):
        books = [book.title for book in self._books if not book._is_checked_out]
        if books:
            print(books)
        else:
            print("No books available")