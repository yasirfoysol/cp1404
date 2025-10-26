"""
CP1404 Assignment 1 - Books to Read
Name:  yasir foysol rahib  
Date Started: 20/10/2025
GitHub URL: https://github.com/cp1404-students/a1-books-yasirfoysol.git
"""

import csv

# Constants

FILENAME = "books.csv"
MENU = """Menu:
D - Display books
A - Add a new book
C - Complete a book
Q - Quit
>>> """
STATUS_UNREAD = "u"
STATUS_COMPLETED = "c"

# Main Function

def main():
    """Main program for Books to Read 1.0."""
    print("Books to Read 1.0 by Yasir Foysol Rahib")

    books = load_books(FILENAME)
    print(f"{len(books)} books loaded.\n")

    choice = input(MENU).strip().lower()
    while choice != "q":
        if choice == "d":
            display_books(books)
        elif choice == "a":
            add_book(books)
        elif choice == "c":
            complete_book(books)
        else:
            print("Invalid menu choice")
        print()
        choice = input(MENU).strip().lower()

    save_books(FILENAME, books)
    print(f"{len(books)} books saved to {FILENAME}")
    print('"So many books, so little time. Frank Zappa"')


# Function Definitions

def load_books(filename):
    """Load books from a CSV file into a list of lists."""
    books = []
    try:
        with open(filename, "r", encoding="utf-8") as in_file:
            reader = csv.reader(in_file)
            for row in reader:
                row[2] = int(row[2])
                books.append(row)
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty list.")
    return books


def save_books(filename, books):
    """Save books to the CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as out_file:
        writer = csv.writer(out_file)
        for book in books:
            writer.writerow(book)


def display_books(books):
    """Display all books, sorted by author then title."""
    if not books:
        print("No books found.")
        return

    books.sort(key=lambda b: (b[1].lower(), b[0].lower()))
    max_title = max(len(book[0]) for book in books)
    max_author = max(len(book[1]) for book in books)

    unread_books = [b for b in books if b[3] == STATUS_UNREAD]
    total_unread_pages = sum(b[2] for b in unread_books)

    for i, book in enumerate(books, start=1):
        marker = "*" if book[3] == STATUS_UNREAD else " "
        print(f"{marker} {i}. {book[0]:<{max_title}} by {book[1]:<{max_author}}  {book[2]:>4} pages")

    if unread_books:
        print(f"You still need to read {total_unread_pages} pages in {len(unread_books)} books.")
    else:
        print("No books left to read. Why not add a new book?")


def add_book(books):
    """Add a new unread book to the list with input validation."""
    title = get_non_empty_input("Title: ")
    author = get_non_empty_input("Author: ")
    pages = get_positive_int("Number of Pages: ")

    new_book = [title, author, pages, STATUS_UNREAD]
    books.append(new_book)
    print(f"{title} by {author} ({pages} pages) added.")


def complete_book(books):
    """Mark a selected unread book as completed."""
    unread_books = [b for b in books if b[3] == STATUS_UNREAD]
    if not unread_books:
        print("No unread books - well done!")
        return

    display_books(books)
    print("Enter the number of a book to mark as completed")

    book_index = get_valid_book_number(books)
    selected_book = books[book_index]
    if selected_book[3] == STATUS_COMPLETED:
        print("That book is already completed")
    else:
        selected_book[3] = STATUS_COMPLETED
        print(f"{selected_book[0]} by {selected_book[1]} completed!")


# Input Helper Functions

def get_non_empty_input(prompt):
    """Prompt for a non-empty string."""
    user_input = input(prompt).strip()
    while not user_input:
        print("Input can not be blank")
        user_input = input(prompt).strip()
    return user_input


def get_positive_int(prompt):
    """Prompt for a positive integer."""
    while True:
        user_input = input(prompt)
        try:
            number = int(user_input)
            if number <= 0:
                print("Number must be > 0")
            else:
                return number
        except ValueError:
            print("Invalid input - please enter a valid number")


def get_valid_book_number(books):
    """Prompt for a valid book number."""
    while True:
        user_input = input(">>> ")
        try:
            number = int(user_input)
            if number <= 0:
                print("Number must be > 0")
            elif number > len(books):
                print("Invalid book number")
            else:
                return number - 1
        except ValueError:
            print("Invalid input - please enter a valid number")


# Program Entry Point

if __name__ == "__main__":
    main()


