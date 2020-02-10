class MyBook(Book):  # noqa
    def __init__(self, title, author, price):
        super(Book, self).__init__()  # noqa
        self.price = price

    def display(self):
        print("Title:", title)  # noqa
        print("Author:", author)  # noqa
        print("Price:", price)  # noqa
