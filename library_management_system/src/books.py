class Book:
    def __init__(self, book_id: str, title: str, author: str, available_count: int):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available_count = available_count

    def __repr__(self):
        return (f"Book{{ID='{self.book_id}', title='{self.title}', "
                f"author='{self.author}', available={self.available_count}}}")

def find_book_by_id(book_id: str, books) -> Book:
    for b in books:
        if b.book_id == book_id:
            return b
    return None
