"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name='', surname='', position=''):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': 0, 'bonus': 0}


class Position(Worker):
    def get_full_name(self):
        if self.name == '':
            self.name = input(f'Enter name: ')
        if self.surname == '':
            self.surname = input('Enter surname: ')

    def get_total_income(self):
        for inc in self._income:
            self._income.update({inc: float(input(f'Enter {inc}: '))})


print(Worker.__dict__)
print(Position.__dict__)
pos1 = Position()
print('pos1 in: ', pos1.__dict__)
pos1.get_full_name()
print('pos1 get_full_name out: ', pos1.__dict__)
pos1.get_total_income()
print('pos1 get_total_income out: ', pos1.__dict__)
pos2 = Position()
print('pos2 in: ', pos2.__dict__)
pos2.get_full_name()
print('pos2 get_full_name out: ', pos2.__dict__)
pos2.get_total_income()
print('pos2 get_total_income out: ', pos2.__dict__)
