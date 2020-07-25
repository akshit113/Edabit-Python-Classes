class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_title(self):
        str_title = 'Title: {}'.format(str(self.title))
        return str_title

    def get_author(self):
        str_author = 'Author: {}'.format(str(self.author))
        return str_author


PP = Book('Pride and Prejudice', 'Jane Austen')
H = Book('Hamlet', 'William Shakespeare')
WP = Book('War and Peace', 'Leo Tolstoy')
