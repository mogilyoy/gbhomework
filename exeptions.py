
from types import NoneType

class Error(Exception):
    def __init__(self, error):
        self.error = error
    

def error_check(subunit = None, name=None, eq_type=None, quantity=None):
    
    if type(subunit) != str and type(subunit) != NoneType:
        raise Error('Подразделение должно иметь строковый тип данных')
    elif type(name) != str and type(name) != NoneType:
        raise Error('Имя техники должно иметь строковый тип данных')
    elif type(eq_type) != str and type(eq_type) != NoneType:
        raise Error('Вид техники должен иметь строковый тип данных')
    elif type(quantity) != int and type(quantity) != NoneType:
        raise Error('Количество техники нужно задавать числом')
    else: 
        print('Данные проверены')




