# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractclassmethod


class AbstractClothes:
    @abstractclassmethod
    def __init__(self, param):
        self.param = param
        pass

    @abstractclassmethod
    def expence(self, param):
        self.param = param
        pass

class Clothes(AbstractClothes):

    def __init__(self, name = None):
        self.name = name

    def expence(self, size):
        self.size = size


class Coat(Clothes):
    def __init__(self, name = None):
        self.name = name

    def expence(self, size):
        self.exp = round((size/6.5 + 0.5), 1)
        return self.output
        
    @property
    def output(self):
        if self.name != None:
            print(f'На костюм {self.name} нужно {self.exp} метров ткани')
            return self.exp


        else:
            print(f'На ваш костюм нужно {self.exp} метров ткани')
            return self.exp



class Suit(Clothes):
    def __init__(self, name = None):
        self.name = name

    def expence(self, size):
        self.exp = round((size*2 + 0.3), 1)
        return self.output
        
    @property
    def output(self):
        if self.name != None:
            print(f'На костюм {self.name} нужно {self.exp} метров ткани')
            return self.exp
        else:
            print(f'На ваш костюм нужно {self.exp} метров ткани')
            return self.exp


coat = Coat()
suit = Suit('Том Форд')
coat_expence = coat.expence(48)
suit_expence = suit.expence(1.1)
print(f'Всего нужно {coat_expence + suit_expence} метров ткани')

