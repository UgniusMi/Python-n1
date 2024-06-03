from datetime import datetime

class Reader:
    def __init__(self, book_title, reader_name, borrow_date, return_date):
        self.book_title = book_title
        self.reader_name = reader_name
        self.borrow_date = borrow_date
        self.return_date = return_date

    def is_overdue(self):
        return datetime.now().date().strftime("%Y-%m-%d") > self.return_date