import pickle
import os
from datetime import date

# Update the file paths
USERS_FILE = "../data/users.pkl"
BOOKS_FILE = "../data/books.pkl"
BORROWS_FILE = "../data/borrows.pkl"

def load_data():
    """Load users, books, and borrows from pickle files (if they exist)."""
    users, books, borrows = [], [], []

    # Load Users
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, "rb") as f:
                users = pickle.load(f)
        except Exception:
            print("خطا در بارگذاری فایل کاربران (Could not load users).")

    # Load Books
    if os.path.exists(BOOKS_FILE):
        try:
            with open(BOOKS_FILE, "rb") as f:
                books = pickle.load(f)
        except Exception:
            print("خطا در بارگذاری فایل کتاب ها (Could not load books).")

    # Load Borrows
    if os.path.exists(BORROWS_FILE):
        try:
            with open(BORROWS_FILE, "rb") as f:
                borrows = pickle.load(f)
        except Exception:
            print("خطا در بارگذاری فایل امانت ها (Could not load borrows).")
    
    return users, books, borrows

def save_data(users, books, borrows):
    """Save users, books, and borrows into pickle files."""
    try:
        with open(USERS_FILE, "wb") as f:
            pickle.dump(users, f)
    except Exception:
        print("خطا در ذخیره فایل کاربران (Could not save users).")

    try:
        with open(BOOKS_FILE, "wb") as f:
            pickle.dump(books, f)
    except Exception:
        print("خطا در ذخیره فایل کتاب ها (Could not save books).")

    try:
        with open(BORROWS_FILE, "wb") as f:
            pickle.dump(borrows, f)
    except Exception:
        print("خطا در ذخیره فایل امانت ها (Could not save borrows).")
