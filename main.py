import sys
from datetime import datetime, timedelta
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


def search_client_by_id(id_no):
    for client in clients:
        if client.get_id_no() == id_no:
            return client


def borrow_book():
    show_books()
    user_choice = int(input('please choose a book for borrowing :  '))
    if books[user_choice - 1].get_status() == 'Inactive':
        print('sorry the book is already borrowed')
    else:
        id_no = input('please enter your id number :  ')
        client = search_client_by_id(id_no)
        if client is not None:
            interval = input('please enter number of days for borrowing :  ')
            borrowed_order = BorrowingOrder(id_no, books[user_choice - 1].get_id(), interval, )
            borrowed_orders.append(borrowed_order)
            books[user_choice - 1].change_status()
        else:
            print(f'there is no user with id:  {id_no}')


def return_book():
    id_no = input('please enter your id number :  ')
    client = search_client_by_id(id_no)
    if client is not None:
        user_borrowed_books = []
        for borrowed_order in borrowed_orders:
            if borrowed_order.get_client_id() == id_no and borrowed_order.get_status() == 'Active':
                user_borrowed_books.append(borrowed_order)
        if len(user_borrowed_books) == 0:
            print('there is no active borrowing for this client')
        else:

            for x in range(len(user_borrowed_books)):
                for book in books:
                    if user_borrowed_books[x].get_book_id() == book.get_id():
                        print(f'{x + 1}  {book.get_title()}')
                user_choice = int(input('please choose the book to return it to the library :  '))
                for book in books:
                    if user_borrowed_books[user_choice - 1].get_book_id() == book.get_id():
                        book.change_status()
                for borrowed_order in borrowed_orders:
                    if user_borrowed_books[user_choice - 1].get_book_id() == borrowed_order.get_book_id():
                        borrowed_order.refresh_status()

    else:
        print(f'there is no user with id:  {id_no}')


def show_books():
    print("{:<8} {:<25} {:<10}".format('index', 'title', 'status'))
    for x in range(len(books)):
        print("{:<8} {:<25} {:<10}".format(x + 1, books[x].get_title(), books[x].get_status()))


def show_borrowed_orders():
    print("{:<8} {:<25} {:<10} {:<10}".format('index', 'book id', 'status', 'end date'))
    for x in range(len(borrowed_orders)):
        print("{:<8} {:<25} {:<10} {:<10}".format(x + 1, get_book_title_by_id(borrowed_orders[x].get_book_id()),
                                                  borrowed_orders[x].get_status(),
                                                  str(borrowed_orders[x].get_end_date())))
    print('----------------------------------------------------------------------')


def get_book_title_by_id(book_id):
    for book in books:
        if book.get_id() == book_id:
            return book.get_title()


def handle_choice(user_choice):
    if user_choice == '0':
        exit()
    elif user_choice == '1':
        add_client()
    elif user_choice == '2':
        add_librarian()
    elif user_choice == '3':
        show_borrowed_orders()
    elif user_choice == '4':
        borrow_book()
    elif user_choice == '5':
        return_book()
    else:
        print('wrong choice please try again: ')


# Start execution
Menus().header()
while run:
    choice = Menus().main_menu()
    handle_choice(choice)
