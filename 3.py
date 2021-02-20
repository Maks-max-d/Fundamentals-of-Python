class Nucleus:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        if self.cell - other.cell >= 0:
            return self.cell - other.cell
        else:
            return 'Total less than zero'

    def __mul__(self, other):
        return self.cell * other.cell

    def __truediv__(self, other):
        return self.cell // other.cell

    def make_order(self, row):
        self._row = row
        self.__row1 = ''.join([str('*') for i in range(0, self._row)])
        self.__row2 = ''.join([str('*') for i in range(0, self.cell % self._row)])
        self.__rorder = [self.__row1 for i in range(0, self.cell // self._row)] + [self.__row2]
        return '\n'.join(self.__rorder)

n1 = Nucleus(24)
n2 = Nucleus(5)
print(n1 + n2)
print(n1 - n2)
print(n2 - n1)
print(n1 * n2)
print(n1 / n2)
print(n1.make_order(11))
