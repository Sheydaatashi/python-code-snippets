class Borrow:
    def __init__(self, borrow_id: int, user_id: int, book_id: str,
                 borrow_date: date, due_date: date, is_book_returned: bool):
        self.borrow_id = borrow_id
        self.user_id = user_id
        self.book_id = book_id
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.is_book_returned = is_book_returned

    def __repr__(self):
        status = "برگشته" if self.is_book_returned else "در حال امانت"
        return (f"Borrow{{ID={self.borrow_id}, user={self.user_id}, book='{self.book_id}', "
                f"borrow_date={self.borrow_date}, due_date={self.due_date}, status='{status}'}}")
