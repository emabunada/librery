from person import Person


class Librarian(Person):
    def __init__(self, name, age, id_no, phone_number, salary=0):
        super().__init__(name, age, id_no, phone_number)
        self._salary = salary

    def set_salary(self, salary):
        self._salary = salary

    def get_salary(self):
        return self._salary
