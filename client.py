from person import Person


class Client(Person):
    def __init__(self, name, age, id_no, phone_number):
        super().__init__(name, age, id_no, phone_number)
