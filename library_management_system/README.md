# Library Management System

A simple library management system implemented in Python that allows:
- User authentication and registration
- Book management
- Borrowing and returning books
- Search functionality

## Project Structure
- `src/`: Source code files
  - `main.py`: Entry point of the application
  - `admin.py`: Admin functionality
  - `user.py`: User functionality
  - `books.py`: Book-related operations
  - `borrows.py`: Borrowing system
  - `users.py`: User management
  - `utils.py`: Utility functions

- `data/`: Data storage
  - Contains pickle files for persistent storage

## Setup and Running
1. Ensure Python 3.x is installed
2. Navigate to the project directory
3. Run `python src/main.py`