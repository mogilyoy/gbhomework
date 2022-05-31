# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.


class Complex_number:
    def __init__(self, number):
        if '+' in number:
            self.number = number.replace(' ', '').replace('i', '').split('+')
        elif 'i' in number:
            b = number.replace(' ', '').replace('i', '')
            self.number = [0, b]
        elif int(number):
            self.number = [number, 0]
        else: 
            print('Неправильное значение')

    def __str__(self):
        if self.number[0] == '0':
            return f'{self.number[1]}i'
        elif self.number[1] == '0':
            return f'{self.number[0]}'
        else:
            return f'{self.number[0]}+{self.number[1]}i'

    def __add__(self, other):
        a1 = int(self.number[0])
        a2 = int(other.number[0])
        b1 = int(self.number[1])
        b2 = int(other.number[1])
        return Complex_number(f'{a1 + a2}+{b1 + b2}i')


    def __mul__(self, other):
        a1 = int(self.number[0])
        a2 = int(other.number[0])
        b1 = int(self.number[1])
        b2 = int(other.number[1])
        return Complex_number(f'{a1*a2 - b1*b2}+{a1*b2 +a2*b1}i')

c = '7+8i'
d = '10+10i'
c = Complex_number(c)
d = Complex_number(d)
print(c+d)

