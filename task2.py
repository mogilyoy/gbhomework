# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.



class Road():
    def __init__(self, length, width):
        self._lenght, self._width = length, width
    def massa(self, thick, squaremas):
        self._mas = self._lenght*self._width*thick*squaremas
        return self._mas

lenght = int(input('Введите длину дороги'))
width = int(input('Введите ширину дороги'))
thick = int(input('Введите толщину полотна'))
squaremas = int(input('Сколько кг асфальта нужно на 1 кв метр?'))

a = Road(lenght, width)
print(f'вам нужно {round(a.massa(thick, squaremas)/1000)} т. асфальта ')
