# Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker():
    def __init__(self):
        self.name = 'Билл'
        self.surname = 'Гейтс'
        self.position = 'CEO'
        self.__income = {'wage': 20000, 'bonus': 2000}


class Position(Worker):
    def get_full_name(self):
        self.full_name = f'{self.name} {self.surname}'
        print(f'Сотрудника зовут: {self.full_name}')

    def get_total_income(self):
        self.income = self._Worker__income['wage'] + self._Worker__income['bonus']
        print(f'Сотрудник зарабатывает {self.income} рублей')

position = Position()
position.get_full_name()
position.get_total_income()
print(position.name, position.surname, position.position, position._Worker__income)
