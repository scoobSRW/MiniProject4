import mysql.connector

def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Preffer_2_Leave_Out",
            database="library_db"
        )
        if connection.is_connected():
            print("Successfully connected to the database")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

class Book:
    def __init__(self, title, author_id, isbn, publication_date, availability=True):
        self.title = title
        self.author_id = author_id
        self.isbn = isbn
        self.publication_date = publication_date
        self.availability = availability

    def add_to_db(self, conn):
        cursor = conn.cursor()
        try:
            sql = "INSERT INTO books (title, author_id, isbn, publication_date, availability) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (self.title, self.author_id, self.isbn, self.publication_date, self.availability))
            conn.commit()
            print("Book added successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

    @staticmethod
    def display_all_books(conn):
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM books")
            books = cursor.fetchall()
            if books:
                print("Books in the library:")
                for book in books:
                    print(book)
            else:
                print("No books found.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()


def add_new_book():
    title = input("Enter book title: ")
    author_id = input("Enter author ID: ")
    isbn = input("Enter book ISBN: ")
    publication_date = input("Enter publication date (YYYY-MM-DD): ")
    availability = input("Is the book available? (1 for Yes, 0 for No): ")

    new_book = Book(title, author_id, isbn, publication_date, availability)

    conn = connect_to_db()
    if conn:
        new_book.add_to_db(conn)
        conn.close()


def show_all_books():
    conn = connect_to_db()
    if conn:
        Book.display_all_books(conn)
        conn.close()


def main_menu():
    while True:
        print("\nWelcome to the Library Management System")
        print("1. Add a new book")
        print("2. Display all books")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_new_book()
        elif choice == '2':
            show_all_books()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main_menu()
