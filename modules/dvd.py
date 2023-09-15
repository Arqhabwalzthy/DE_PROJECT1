from modules.library_item import Libraryitem


class Dvd(Libraryitem):
    def __init__(self, title, upc, subject, actors, directors, genre):
        super().__init__(title, upc, subject)
        self.actors = actors
        self.directors = directors
        self.genre = genre
