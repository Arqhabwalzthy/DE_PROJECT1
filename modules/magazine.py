from modules.library_item import Libraryitem

class Magazine(Libraryitem):
    def __init__(self, title, upc, subject, volume, issue):
        super().__init__(title, upc, subject)
        self.volume = volume
        self.issue = issue