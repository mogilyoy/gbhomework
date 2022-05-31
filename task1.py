# Pеализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    date = None
    def __init__(self, date):
        self.date = date
        Date.date = date

    @classmethod
    def date_order(cls):
        date = cls.date.split('-')
        if cls.date_valid(date):
            for i in range(0, len(date)):
                date[i] = int(date[i])
            return date
        else:
            return 'DateFormatError'
    
    @staticmethod
    def date_valid(date):
        year = {
            '01':31,
            '02':28,
            '03':31,
            '04':30,
            '05':31,
            '06':30,
            '07':31,
            '08':31,
            '09':30,
            '10':31,
            '11':30,
            '12':31,
        }

        if date[1] not in year:
            print('Неправильный формат месяца')
            return False
        elif int(date[2]) > 2022:
            print('Неправильный формат года')
            return False
        elif int(date[0]) > year[date[1]]:
            print('Неправильный формат числа')
            return False
        else:
            return True



data = Date('02-10-2021')
print(data.date_order())


