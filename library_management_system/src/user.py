from books import *
from borrows import *
from utils import save_data

def user_menu(user, users, books, borrows):
    while True:
        print("\n=== منوی کاربر (User Menu) ===")
        print("1. جستجوی کتاب در لیست موجود (Search books)")
        print("2. امانت گرفتن کتاب (Borrow a book)")
        print("3. مشاهده کتاب هایی که امانت گرفته ام (View my borrowed books)")
        print("4. بازگشت کتاب (Return a book)")
        print("5. بازگشت (Go back to main menu)")
        choice = input("گزینه را انتخاب کنید: ").strip()

        if choice == "1":
            search_books(books)
        elif choice == "2":
            borrow_book(user, books, borrows)
        elif choice == "3":
            view_my_borrows(user, borrows, books)
        elif choice == "4":
            return_book(user, borrows, books)
        elif choice == "5":
            break
        else:
            print("گزینه نامعتبر است!")

        save_data(users, books, borrows)

def search_books(books):
    keyword = input("عبارت مورد جستجو را وارد کنید (Enter search keyword): ").strip().lower()
    results = []
    for b in books:
        if keyword in b.title.lower() or keyword in b.author.lower():
            results.append(b)

    if not results:
        print("هیچ کتابی یافت نشد (No books found).")
    else:
        print("نتایج جستجو (Search results):")
        for r in results:
            print(r)

def borrow_book(user, books, borrows):
    book_id = input("شناسه کتابی که می خواهید امانت بگیرید را وارد کنید (Enter book ID to borrow): ").strip()
    book = find_book_by_id(book_id, books)
    if not book:
        print("کتابی با این شناسه وجود ندارد (Book not found).")
        return
    if book.available_count <= 0:
        print("هیچ نسخه ای از این کتاب در حال حاضر موجود نیست (No copies available).")
        return

    new_borrow_id = (max([br.borrow_id for br in borrows]) + 1) if borrows else 1
    borrow_date = date.today()
    due_date = borrow_date + timedelta(weeks=2)

    new_borrow = Borrow(new_borrow_id, user.user_id, book.book_id,
                        borrow_date, due_date, False)
    borrows.append(new_borrow)
    book.available_count -= 1
    print("کتاب با موفقیت امانت گرفته شد (Book borrowed successfully).")

def view_my_borrows(user, borrows, books):
    print("\n--- کتاب های امانت گرفته شده توسط شما (Your borrowed books) ---")
    found_any = False
    for br in borrows:
        if br.user_id == user.user_id and not br.is_book_returned:
            book = find_book_by_id(br.book_id, books)
            if book:
                print(f"BorrowID: {br.borrow_id} | کتاب: {book.title} "
                      f"| تاریخ امانت: {br.borrow_date} | موعد بازگشت: {br.due_date}")
                found_any = True

    if not found_any:
        print("شما در حال حاضر هیچ کتابی امانت نگرفته اید (No borrowed books).")

def return_book(user, borrows, books):
    try:
        borrow_id = int(input("شناسه امانت (Borrow ID) را وارد کنید (Enter the borrow ID to return the book): "))
    except ValueError:
        print("خطا در ورودی (Invalid input).")
        return

    to_return = None
    for br in borrows:
        if br.borrow_id == borrow_id and br.user_id == user.user_id and not br.is_book_returned:
            to_return = br
            break

    if to_return:
        to_return.is_book_returned = True
        book = find_book_by_id(to_return.book_id, books)
        if book:
            book.available_count += 1
        print("کتاب برگشت داده شد (Book returned successfully).")
    else:
        print("رکورد امانتی یافت نشد یا قبلاً برگشت داده شده است (Borrow record not found or already returned).")
