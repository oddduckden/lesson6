"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
(отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""


class Stationery:
    def __init__(self, title=''):
        self.title = title

    def draw(self):
        print('запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Pen: запуск отрисовки {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Pencil: запуск отрисовки {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Handle: запуск отрисовки {self.title}')


a = Stationery()
print('Class Stationery')
a.draw()
b = Pen('ручка')
print(b.__dict__)
print('Class Pen')
b.draw()
c = Pencil('карандаш')
print('Class Pencil')
c.draw()
d = Handle('маркер')
print('Class Handle')
d.draw()
