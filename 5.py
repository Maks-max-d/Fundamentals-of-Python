class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки (Pen).')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки (Pencil).')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки (Handle).')


s = Stationery('1')
s.draw()

s = Pen('2')
s.draw()

s = Pencil('3')
s.draw()

s = Handle('4')
s.draw()
