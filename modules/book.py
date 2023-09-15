from modules.library_item import Libraryitem


class Book(Libraryitem):
    def __init__(self, isbn, authors, title, subject, dds_number, upc):
        Libraryitem.__init__(self, title, upc, subject)
        self.isbn = isbn
        self.author = authors
        self.dds_number = dds_number