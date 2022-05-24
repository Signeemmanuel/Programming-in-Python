# this file aims to illustrate the concept of inheritance and polymorphism in python

class Publication:
    # creation of publication object
    def __init__(self, code, title, author):
        self._code = code
        self._title = title
        self._author = author

    # get the code of the publication
    def get_code(self):
        return self._code

    # Returns a string containing a formatted bibliography entry.
    def get_bib_entry(self):
        return '[' + self._code + '] "' + self._title + '"  by ' + self._author

    def __str__(self):
        return self.get_bib_entry()


class Book(Publication):
    # creation of book object
    def __init__(self, code, title, author, publisher, year):
        super().__init__(code, title, author)
        self._publisher = publisher
        self._year = year

    # return string of formatted entries
    def get_bib_entry(self):
        return super().get_bib_entry() + ', Published by ' + self._publisher + ', ' + self._year


class Chapter(Book):
    # Creating chapter object
    def __init__(self, code, title, author, publisher, year, chapter, pages):
        super().__init__(code, title, author, publisher, year)
        self._chapter = chapter
        self._pages = pages

    # return string of formatted entry
    def get_bib_entry(self):
        return super().get_bib_entry() + ', Chapter ' + str(self._chapter) + ' pp. ' + self._pages


class Article(Publication):
    # Creating Article object
    def __init__(self, code, title, author, journal, volume, number, year):
        super().__init__( code, title, author )
        self._journal = journal
        self._volume = volume
        self._number = number
        self._year = year

    # return string of formatted entry
    def get_bib_entry( self ):
        return super().get_bib_entry() + self._journal + self._volume + self._year


chap = Chapter("Smith90", "The Year that Was", "John Smith", "Bookends Publishing", "1990", "2", "32")
print(chap.get_bib_entry())
print(chap)
