# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
import traceback

class IncorrectDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt

def div(a, b):
    return a/b

try:
    a = int(input('Введите 1 число'))
    b = int(input('Введите 2 число'))
    if b == 0:
        raise IncorrectDivisionError('You are  trying to divide by zero!')
    else:
        print(round(div(a, b)))
        
except IncorrectDivisionError as error:
    print(f'{IncorrectDivisionError.__name__}: {error}')






