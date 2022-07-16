from datetime import datetime
from random import randint


class Person:
    def __init__(self, name, age, id_no, phone_number):
        self._id = self._set_id()
        self._name = name
        self._age = age
        self._id_no = id_no
        self._phone_number = phone_number

    def _set_id(self):
        return str(datetime.now()).replace('-', '').split(' ')[0] + \
               str(datetime.now()).replace(':', '').split(' ')[1].split('.')[0] + str(randint(0, 1000))

    def get_id(self):
        return self._id

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_age(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_id_no(self, id_no):
        self._id_no = id_no

    def get_id_no(self):
        return self._id_no

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def get_phone_number(self):
        return self._phone_number
