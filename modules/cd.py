from modules.library_item import Libraryitem

class Cd(Libraryitem):
    def __init__(self, title, upc, subject, artist):
        super(). __init__(title, upc, subject)
        self.artist = artist 