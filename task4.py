"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
(булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed=0, color='', name='', is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print('Текущая скорость:', self.speed)


class TownCar(Car):
    def show_speed(self):
        print('Скорость превышена' if self.speed > 60 else f'Текущая скорость: {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        print('Скорость превышена' if self.speed > 40 else f'Текущая скорость: {self.speed}')


class SportCar(Car):
    sparco = True


class PoliceCar(Car):
    def flashing_light(self):
        print('flashing_light is on')


car1 = TownCar(80, 'white', 'Reno', False)
print(f'Car1 name: {getattr(car1, "name")}')
print(car1.__dict__)
car1.go()
car1.show_speed()
car1.turn('left')
car2 = TownCar(60, 'grey', 'Toyota', False)
print(f'Car2 name: {car2.name}')
print(car2.__dict__)
car2.go()
car2.show_speed()
car2.stop()
car3 = SportCar(120, 'red', 'BMW')
print(car3.__dict__)
print(f'Car3 name: {car3.name} color: {car3.color}')
car3.show_speed()
car1.turn('right')
car4 = PoliceCar(120, 'white', 'Toyota', True)
print(f'Car2 name: {car4.name}')
print(car4.__dict__)
car4.go()
car4.flashing_light()
car1.turn('right')
car4.show_speed()
car1.turn('right')
