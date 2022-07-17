from client import Client
from book import Book
from borrowing_order import BorrowingOrder
from menus import Menus

clients = [Client('mohammed', 22, '805698744', '0598756322'), Client('Khaled', 18, '405688799', '0568744158'),
           Client('Alaa', 30, '700598776', '0592478965'), Client('Khalil', 25, '778410259', '0598753214'), ]
books = [Book('Java how to program', 'Paul Deitel', ), Book('Queen of Fire', 'Devika Rangachari', ),
         Book('The India Story', '	Bimal Jalal', ), Book('Hear Yourself', 'Prem Rawat', ),
         Book('A Place Called Home', 'Preeti Shenoy', )]
Menus().main_menu()
