import mysql.connector

def add_book(conn):
    title= input("Enter book title: ")
    author= input("Enter author: ")
    cursor= conn.cursor()
    cursor.execute("INSERT INTO BOOKS (title, author) VALUES (%s, %s)", (title, author))
    conn.commit()
    print(f"Book '{title}' is added!\n")

def view_books(conn, only_available=False):
    cursor= conn.cursor()
    if only_available:
        cursor.execute("Select * from books where available='yes'")
    else:
        cursor.execute("Select * from books")
    books= cursor.fetchall()
    if not books:
        print("No books found!\n")
        return
    
    print("\n--- Books in Library ---")
    for b in books:
        print(f"{b[0]} | {b[1]} | {b[2]} | Available: {b[3]}")
    print("-----------------------\n")

def borrow_book(conn):
    cursor= conn.cursor()
    title= input("Enter book title to borrow: ")
    cursor.execute("SELECT available FROM books WHERE title=%s", (title,))
    result= cursor.fetchone()
    if not result:
        print("Book not found!\n")
        return
    if result[0]=="no":
        print("Book already borrowed!\n")
        return
    print(f"You borrowed '{title}'\n")
    cursor.execute("UPDATE books SET available='no' WHERE title=%s", (title,))
    conn.commit()

def return_book(conn):
    cursor= conn.cursor()
    title= input("Enter book title to return: ")
    cursor.execute("SELECT available FROM books WHERE title=%s", (title,))
    result= cursor.fetchone()
    if not result:
        print("Book not found!\n")
        return
    if result[0]=="yes":
        print("Book is already in library!\n")
        return
    print(f"You returned '{title}'\n")
    cursor.execute("UPDATE books SET available='yes' WHERE title=%s", (title,)) 
    conn.commit()

def main():
    conn= mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="library"  # type: ignore
    )
    cursor= conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS library")
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS books
                   (id INT PRIMARY KEY AUTO_INCREMENT,
                   title VARCHAR(100),
                   author VARCHAR(100),
                   available ENUM('yes','no') DEFAULT 'yes')
                   """)
    conn.commit()

    while True:
        print("1. Add books  2. View all books 3. View available books  4. Borrow  5. Return  6. Exit")
        choice = input("Enter your choice:")
        if choice =="1":
            add_book(conn)
        elif choice =="2":
            view_books(conn)
        elif choice =="3":
            view_books(conn, only_available=True)
        elif choice =="4":
            borrow_book(conn)
        elif choice =="5":
            return_book(conn)
        elif choice=="6":
            print("Exiting...")
            break
        else:
            print("Invalid choice!\n")
        

if __name__ == "__main__":
    main()