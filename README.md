# 📚 Library Management System

A console-based Library Management System built using **Python** and **MySQL**.  
This project allows users to add books, view books, borrow and return books while tracking availability using a database.

## ✨ Features
- Add books  
- View all / available books  
- Borrow and return books  
- MySQL database integration  

## 🛠 Tech Stack
- Python  
- MySQL  
- mysql-connector-python  

## ⚙️ How the Code Works
- The program connects to a MySQL database using `mysql.connector`.
- On startup, it creates a database (`library`) and a table (`books`) if they don’t already exist.
- The application runs in a menu-driven loop, allowing the user to choose actions.

### Function Breakdown
- `add_book()` → Adds a new book to the database.
- `view_books()` → Displays all books or only available books.
- `borrow_book()` → Marks a book as borrowed if available.
- `return_book()` → Marks a borrowed book as available again.
- `main()` → Handles database setup and controls the program flow.

- Book availability is tracked using an `available` field (`yes` / `no`).
- All changes are committed to the database to ensure data persistence.
