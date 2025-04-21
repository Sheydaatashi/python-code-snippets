from users import *
from books import *
from borrows import *
from utils import save_data

def admin_menu(users, books, borrows):
    while True:
        print("\n=== منوی مدیر (Admin Menu) ===")
        print("1. مدیریت کاربران (Manage Users)")
        print("2. مدیریت کتاب ها (Manage Books)")
        print("3. مشاهده وضعیت امانت ها (View borrowed books)")
        print("4. بازگشت (Go back to main menu)")
        choice = input("گزینه را انتخاب کنید: ").strip()

        if choice == "1":
            manage_users(users)
        elif choice == "2":
            manage_books(books)
        elif choice == "3":
            view_borrows(borrows, users, books)
        elif choice == "4":
            break
        else:
            print("گزینه نامعتبر است!")

        save_data(users, books, borrows)

def manage_users(users):
    while True:
        print("\n-- مدیریت کاربران (Manage Users) --")
        print("1. افزودن کاربر جدید (Add new user)")
        print("2. حذف کاربر (Delete user)")
        print("3. مشاهده لیست کاربران (View all users)")
        print("4. بازگشت (Go back)")
        choice = input("گزینه را انتخاب کنید: ").strip()

        if choice == "1":
            register_user(users)
        elif choice == "2":
            delete_user(users)
        elif choice == "3":
            list_users(users)
        elif choice == "4":
            break
        else:
            print("گزینه نامعتبر است!")

        save_data(users)

def delete_user(users):
    try:
        user_id = int(input("شناسه کاربر را برای حذف وارد کنید (Enter user ID to delete): "))
    except ValueError:
        print("خطا در ورودی (Invalid input).")
        return

    to_remove = next((u for u in users if u.user_id == user_id), None)
    if to_remove:
        users.remove(to_remove)
        print("کاربر حذف شد (User removed).")
    else:
        print("کاربری با این شناسه پیدا نشد (No user found with that ID).")

def list_users(users):
    print("\n--- فهرست کاربران (Users List) ---")
    for u in users:
        print(u)
