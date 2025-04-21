from utils import load_data
from admin import admin_menu
from user import user_menu

def main():
    # Load data from files
    users, books, borrows = load_data()

    while True:
        print("\nسیستم مدیریت کتابخانه (Library Management System)")
        print("1. ورود (Login)")
        print("2. ثبت نام (Register)")
        print("3. خروج (Exit)")
        choice = input("گزینه را انتخاب کنید (Choose an option): ").strip()

        if choice == "1":
            username = input("نام کاربری: ").strip()
            password = input("رمز عبور: ").strip()
            if username == "admin" and password == "admin123":
                admin_menu(users, books, borrows)
            else:
                user = find_user_by_credentials(username, password, users)
                if user:
                    user_menu(user, users, books, borrows)
                else:
                    print("نام کاربری یا رمز عبور اشتباه است!")
        elif choice == "2":
            # Handle registration (implement as needed)
            pass
        elif choice == "3":
            print("خروج از برنامه. موفق باشید!")
            break
        else:
            print("گزینه نامعتبر است (Invalid option)")

    save_data(users, books, borrows)

if __name__ == "__main__":
    main()
