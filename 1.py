from itertools import cycle
import time

class TrafficLight:
    def running(self, color, shift):
        self.__colorlist = ['Red', 'Yellow', 'Green']
        self.__color = color
        self.__shift = shift
        # проверка, что цвет из списка
        if self.__color not in ['Red', 'Yellow', 'Green']:
            self.__color = 'Red'
        # проверка, что кол-во переключений > 1
        if self.__shift < 1:
            self.__shift = 1
        # формируем список с цветами в правильном порядке
        self.__colorlist = self.__colorlist[self.__colorlist.index(self.__color):3] + self.__colorlist[0:self.__colorlist.index(self.__color)]
        # цикл
        for el in cycle(self.__colorlist):
            print(el)
            if el == 'Red':
                time.sleep(7)
            elif el == 'Yellow':
                time.sleep(2)
            else:
                time.sleep(4)
            self.__shift -= 1
            if self.__shift <= 0:
                break

tl = TrafficLight()
tl.running('Green', 7) # Запускаем с зеленого, 7 переключений
