class Book:
    def __init__(self, name, author, page):
        self.name = name
        self.author = author
        self.page = page

    def __str__(self):
        return f'{self.name} - {self.author} - {self.page}'

b1 = Book('jhjh','ghjgjh',45)
b2 = Book('qeqe', 'iutee', 55)
print(b1)
print(b2)
