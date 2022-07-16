from client import Client
from borrowing_order import BorrowingOrder

c = Client('ahmed', 18, 'asdsadas', '6545646464')
b = BorrowingOrder('1', '2', 20, )
print(b.get_end_date())
