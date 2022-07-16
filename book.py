from datetime import datetime
from random import randint


class Book:
    def __init__(self, title, auther, status='Active'):
        self._id = self._set_id()
        self._title = title
        self._auther = auther
        self._status = status

    def _set_id(self):
        return str(datetime.now()).replace('-', '').split(' ')[0] + \
               str(datetime.now()).replace(':', '').split(' ')[1].split('.')[0] + str(randint(0, 1000))

    def get_id(self):
        return self._id

    def set_title(self, title):
        self._title = title

    def get_title(self):
        return self._title

    def set_auther(self, auther):
        self._auther = auther

    def get_auther(self):
        return self._auther

    def set_status(self, status):
        self._status = status

    def get_status(self):
        return self._status
