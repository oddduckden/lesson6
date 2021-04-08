"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
завершать скрипт.
"""

class TrafficLight:
    def __init__(self, __green=4):
        self.__lt = {'red': 7, 'yellow': 2, 'green': __green}
        self.__color = 'red'

    def running(self):
        for self.__color in self.__lt:
            print(self.__color)
            print('start: ', time.time())
            time.sleep(self.__lt.get(self.__color))
            print('stop: ', time.time())


class TrafficLightUnit:
    def __init__(self, __green=4):
        self.__lt = {'red': 7, 'yellow': 2, 'green': __green}
        self.__nextcolor = -1

    def running_one_light(self, color):
        self.__color = color
        if self.__color != self.__nextcolor and self.__nextcolor != -1:
            print('malfunction, wrong sequence of colors')
            sys.exit(0)
        print(self.__color)
        print('start: ', time.time())
        time.sleep(self.__lt.get(self.__color))
        print('stop: ', time.time())
        __pointer = ['red', 'yellow', 'green'].index(self.__color)
        self.__nextcolor = ['red', 'yellow', 'green'][(0, __pointer + 1)[__pointer != 2]]


auto_light = TrafficLight()
auto_light.running()
print('\nlight color control')
one_light = TrafficLightUnit()
for lg in ('red', 'yellow', 'green'):
    one_light.running_one_light(lg)
