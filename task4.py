# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.


class Car():
    def __init__(self):
        self.speed = None
        self.color = None
        self.name = None
        self.is_police = False
        self.directions = ['запад', 'север', 'восток', 'юг']
        self.dir_state = self.directions[1] # по умолчанию машина едет на север

    def go(self, speed):
        self.speed = speed
        print(f'Стартуем! Текущая скорость машины: {speed}')

    def stop(self):
        self.speed = 0
        print('Приехали! Машина стоит на месте')

    def turn(self, direction):
        if direction == 'right' or direction == 'r':
            if self.speed != 0:
                self.dir_state = self.directions[self.directions.index(self.dir_state)+1]  
                # если мы поворачиваем направо, то смещаемся на один элемент вправо
                print(f'Поворот направо, теперь машина едет на {self.dir_state}')
            else:
                print('Машина стоит на месте, не могу повернуть')
        elif direction == 'left' or direction == 'l':
            if self.speed != 0:
                self.dir_state = self.directions[self.directions.index(self.dir_state)-1]  
                # если мы поворачиваем налево, то смещаемся на один элемент влево
                print(f'Поворот налево, теперь машина едет на {self.dir_state}')
            else:
                print('Машина стоит на месте, не могу повернуть')
        else:
            print('Непонятно, куда повернуть')

    def show_speed(self):
        print(f'Машина едет со скоростью {Car.speed} км/ч')
    

class TownCar(Car):
    def __init__(self):
        super().__init__()
        self.is_police = False
        self.color = 'blue'
        self.name = 'Town car'
    def show_speed(self):
        if Car.speed >60:
            print(f'Вы едете {self.speed} км/ч. Это слишком быстро!')
        else:
            print(f'Вы едете {self.speed} км/ч. Так держать!')


class WorkCar(Car):
    def __init__(self):
        super().__init__()
        self.is_police = False
        self.color = 'yellow'
        self.name = 'Work car'
    def show_speed(self):
        if Car.speed >40:
            print(f'Вы едете {self.speed} км/ч. Это слишком быстро!')
        else:
            print(f'Вы едете {self.speed} км/ч. Так держать!')


class SportCar(Car):
    def __init__(self):
        super().__init__()
        self.is_police = False
        self.color = 'red'
        self.name = 'Sport car'
    def show_speed(self):
        if Car.speed < 60:
            print(f'Вы едете {self.speed} км/ч. Добавьте газу!')
        else:
            print(f'Вы едете {self.speed} км/ч. Вы точно приедете первым!')


class PoliceCar(Car):
    def __init__(self):
        super().__init__()
        self.is_police = True
        self.color = 'white'
        self.name = 'Police car'
    def show_speed(self):
        if self.speed < 60:
            print(f'Вы едете {self.speed} км/ч. Добавьте газу, преступник уходит!')
        else:
            print(f'Вы едете {self.speed} км/ч. Виу-виу, поймать преступника!')

a = PoliceCar()
a.go(150)
a.turn('r')
a.turn('l')
a.show_speed()
print(a.color)
print(a.name)
print(a.speed)





    



        
            
        


