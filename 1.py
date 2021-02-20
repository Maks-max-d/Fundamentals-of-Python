# Класс для рисования матриц
class Matrix_Drow:
    def __init__(self, s):
        self._s = s
        self._str_list = ''

        for i in range(0, len(self._s)):
            self._str_list += ' '.join([str(x) for x in self._s[i]])
            if i < len(self._s):
                self._str_list = self._str_list + '\n'
        self.matrix_str = f'{self._str_list}'


# Класс Matrix: печать, сложение
class Matrix:
    def __init__(self, s):
        self._s = s
        self._str_list = ''
        self._sum_s = []
        self._sum_s_error = 0

    def __str__(self):
        return Matrix_Drow(self._s).matrix_str

    def __add__(self, other):
        for i in range(0, len(self._s)):
            if len(self._s) != len(other):
                self._sum_s_error = 1
            if len(self._s[i]) == len(other[i]):
                self._sum_s.append([k + n for k, n in zip(self._s[i], other[i])])
            else:
                self._sum_s_error = 1
        if self._sum_s_error == 1:
            self._sum_s = []
        return Matrix_Drow(self._sum_s).matrix_str


s1 = [[3, 8, 0, 1], [2, 4, 7, 5], [1, 4, 3, 7]]
s2 = [[4, 8, 3, 7], [7, 8, 4, 3], [1, 5, 3, 1]]

m = Matrix(s1)
print(m)
print(m + s2)
