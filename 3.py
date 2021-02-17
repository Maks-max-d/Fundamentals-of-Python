class Worker:
    def __init__(self, name, surname, position, w_b):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = w_b

class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return w_b.get('wage') + w_b.get('bonus')

name = 'Ivan'
surname = 'Ivanov'
position = 'Senior manager'
w_b = {'wage': 50000, 'bonus': 25000}

w = Position(name, surname, position, w_b)
print(w.get_full_name())
print(w.get_total_income())
