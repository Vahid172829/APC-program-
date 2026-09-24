class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print()


books = [
    Book(1, "Python Programming", "John Smith", 450),
    Book(2, "Data Structures", "Robert Brown", 550),
    Book(3, "Computer Networks", "Andrew Tanenbaum", 650)
]

for book in books:
    book.display()
