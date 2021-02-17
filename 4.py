class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Go')

    def stop(self):
        print('Stop')

    def turn(self, direction):
        print(f'Turn to {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Over speed (town car)!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Over speed (work car)!')

class PoliceCar(Car):
    pass


speed = 80
color = 'black'
name = 'BMW'
is_police = 0

c = Car(speed, color, name, is_police)
c.go()
c.stop()
c.turn('left')
c.show_speed()

c1 = TownCar(speed, color, name, is_police)
c1.show_speed()

c2 = SportCar(speed, color, name, is_police)

c3 = WorkCar(speed, color, name, is_police)
c3.show_speed()

c4 = PoliceCar(speed, color, name, is_police)
