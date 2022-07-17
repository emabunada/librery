import sys

from client import Client
from book import Book
from borrowing_order import BorrowingOrder
from menus import Menus
from librarian import Librarian

clients = [Client('mohammed', 22, '805698744', '0598756322'), Client('Khaled', 18, '405688799', '0568744158'),
           Client('Alaa', 30, '700598776', '0592478965'), Client('Khalil', 25, '778410259', '0598753214'), ]
books = [Book('Java how to program', 'Paul Deitel', ), Book('Queen of Fire', 'Devika Rangachari', ),
         Book('The India Story', '	Bimal Jalal', ), Book('Hear Yourself', 'Prem Rawat', ),
         Book('A Place Called Home', 'Preeti Shenoy', )]
borrowed_orders = []
librarians = []

run = True


def total_borrowed_book():
    count = 0
    for book in books:
        if book.get_status() == 'Inactive':
            count += 1
    return count


total_borrowed_orders = len(borrowed_orders)


def total_available_book():
    count = 0
    for book in books:
        if book.get_status() == 'Active':
            count += 1
    return count


def add_client():
    name = input('please enter client name:  ')
    age = input('please enter client age:  ')
    id_no = input('please enter client identity number:  ')
    phone = input('please enter client phone number:  ')
    clients.append(Client(name, age, id_no, phone))
    print('Client has been added successfully')


def add_librarian():
    name = input('please enter librarian name:  ')
    age = input('please enter librarian age:  ')
    id_no = input('please enter librarian identity number:  ')
    phone = input('please enter librarian phone number:  ')
    salary = input('please enter librarian salary:  ')
    librarians.append(Librarian(name, age, id_no, phone, salary))
    print('Librarian has been added successfully')


def borrow_book():
    show_books()


def return_book():
    pass


def show_books():
    print("{:<8} {:<25} {:<10}".format('index', 'title', 'status'))
    for x in range(len(books)):
        print("{:<8} {:<25} {:<10}".format(x + 1, books[x].get_title(), books[x].get_status()))


def handle_choice(user_choice):
    if user_choice == '0':
        exit()
    elif user_choice == '1':
        add_client()
    elif user_choice == '2':
        add_librarian()
    elif user_choice == '3':
        borrow_book()
    elif user_choice == '4':
        return_book()
    else:
        print('wrong choice please try again: ')


# Start execution

while run:
    Menus().header()
    choice = Menus().main_menu()
    handle_choice(choice)
