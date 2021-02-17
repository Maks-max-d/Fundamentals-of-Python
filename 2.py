class Road:
    def __init__(self):
        self.weight = 25
        self.thickness = 5
        print(f'Weight = {self.weight} kg\n'
              f'Thickness = {self.thickness} cm')

    def _square(self, length, width):
        self._length = length
        self._width = width
        # self.weight = 25  # 25 kg
        # self.thickness = 5  # 5 cm
        return self._length * self._width * self.weight * self.thickness / 1000

r = Road()
print(r._square(5000, 20))
