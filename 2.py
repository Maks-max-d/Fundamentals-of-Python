from abc import ABC, abstractmethod

# Абстрактный класс
class ClothesAbc(ABC):
    def __init__(self, clothes_list):
        self._clothes_list = clothes_list

    @abstractmethod
    def expense(self):
        pass


# Класс-наследник
class clothes(ClothesAbc):
    def expense(self, cl_type=None):
        self._sum_expense = 0
        self._cl_type = cl_type
        for i in range(0, len(self._clothes_list)):
            if self._clothes_list[i]['type'] == 'Пальто' and (self._cl_type == 'Пальто' or self._cl_type == None):
                self._sum_expense += self._clothes_list[i]['V'] / 6.5 + 0.5
            elif self._clothes_list[i]['type'] == 'Костюм' and (self._cl_type == 'Костюм' or self._cl_type == None):
                self._sum_expense += self._clothes_list[i]['H'] * 2 + 0.3
        return round(self._sum_expense, 2)


# Класс-наследник с декоратором
class clothes_sum(clothes):
    @property
    def expense_all(self):
        return clothes(self._clothes_list).expense()

c1 = {'type': 'Пальто', 'V': 40}
c2 = {'type': 'Костюм', 'H': 185}
c3 = {'type': 'Пальто', 'V': 50}
c4 = {'type': 'Костюм', 'H': 180}
c5 = {'type': 'Костюм', 'H': 190}
clothes_list = [c1, c2, c3, c4, c5]

c = clothes(clothes_list)
c1 = c.expense()
c2 = c.expense('Пальто')
c3 = c.expense('Костюм')
print(f'Всего ткани: {c1}\n'
     f'Пальто: {c2}\n'
     f'Костюм: {c3}')

c = clothes_sum(clothes_list)
print(f'Всего ткани (декоратор): {c.expense_all}')
