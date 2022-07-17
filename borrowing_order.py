from datetime import datetime, timedelta
from random import randint


class BorrowingOrder:
    def __init__(self, client_id, book_id, interval_in_days, status='Active'):
        self._id = self.set_id()
        self._client_id = client_id
        self._book_id = book_id
        self._status = status
        self._start_date = datetime.now()
        self._end_date = datetime.date(datetime.now() + timedelta(days=4))

    def set_id(self):
        return str(datetime.now()).replace('-', '').split(' ')[0] + \
               str(datetime.now()).replace(':', '').split(' ')[1].split('.')[0] + str(randint(0, 1000))

    def get_id(self):
        return self._id

    def refresh_status(self):
        if self._end_date >= datetime.now().date():
            self._status = 'canceled'
        elif self._end_date < datetime.now().date():
            self._status = 'Expired'

        else:
            self._status = 'Active'

    def get_status(self):
        return self._status

    def cancel_order(self):
        self._status = 'Canceled'

    def get_client_id(self):
        return self._client_id

    def get_book_id(self):
        return self._book_id

    def get_start_date(self):
        return self._start_date

    def get_end_date(self):
        return self._end_date
