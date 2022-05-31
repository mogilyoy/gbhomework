# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

from exeptions import Error, error_check


structure = {}  
class Warehouse:
    warehouse = {}
    def take_to_subunit(self, subunit, name,  eq_type, quantity):
        print(f'Отправляю в подразделение {subunit} {quantity} ед. техники')
        try:
            error_check(subunit, name, eq_type, quantity)
        except Error as error:
            print(error)

        eq_dict = {'name': name, 'equipment_type': eq_type, 'quantity': quantity}
        if subunit in structure:
            try:
                structure[subunit][f'{name}_{eq_type}']['quantity'] += eq_dict['quantity']
                Warehouse.warehouse[f'{name}_{eq_type}']['quantity'] -= eq_dict['quantity']
                structure['warehouse'] = Warehouse.warehouse
            except KeyError:
                print(f'Нет имени {name}_{eq_type}')
        else:
            try:
                structure[subunit] = {f'{name}_{eq_type}': {'name': name, 'equipment_type': eq_type, 'quantity': quantity}}  
                Warehouse.warehouse[f'{name}_{eq_type}']['quantity'] -= eq_dict['quantity']
                structure['warehouse'] = Warehouse.warehouse
            except KeyError:
                print(f'Нет имени {name}_{eq_type}')

class Equipment:
    counting = {}
    def add_eq(self, name, eq_type, quantity):
        print(f'Добавляю {quantity} ед. техники {eq_type}')
        try:
            error_check(name = name, eq_type = eq_type, quantity= quantity)
        except Error as error:
            print(error)

        eq_dict = {'name': name, 'equipment_type': eq_type, 'quantity': quantity}
        if Equipment.counting:
            if f'{name}_{eq_type}' in Equipment.counting:
                try:
                    Equipment.counting[f'{name}_{eq_type}']['quantity'] += eq_dict['quantity']
                except KeyError:
                    print(f'Нет имени {name}_{eq_type}')
            else:
                Equipment.counting[f'{name}_{eq_type}'] = eq_dict
        else:
            Equipment.counting[f'{name}_{eq_type}'] = eq_dict 


    def lift_to_warehouse(self, name, eq_type, quantity):

        print(f'Отправляю на склад {quantity} ед. техники {eq_type}')
        try:
            error_check(name = name, eq_type = eq_type, quantity= quantity)
        except Error as error:
            print(error)

        eq_dict = {'name': name, 'equipment_type': eq_type, 'quantity': quantity}
        if Warehouse.warehouse:
            if f'{name}_{eq_type}' in Warehouse.warehouse:
                try:
                    Warehouse.warehouse[f'{name}_{eq_type}']['quantity'] += eq_dict['quantity']
                    Equipment.counting[f'{name}_{eq_type}']['quantity'] -= eq_dict['quantity']
                except KeyError:
                    print(f'Нет имени {name}_{eq_type}')

            else:
                try:
                    Warehouse.warehouse[f'{name}_{eq_type}'] = eq_dict
                    Equipment.counting[f'{name}_{eq_type}']['quantity'] -= eq_dict['quantity']
                except KeyError:
                    print(f'Нет имени {name}_{eq_type}')
            
        else:
            try:
                Warehouse.warehouse[f'{name}_{eq_type}'] = eq_dict
                Equipment.counting[f'{name}_{eq_type}']['quantity'] -= eq_dict['quantity']
            except KeyError:
                print(f'Нет имени {name}_{eq_type}')
        

class Printer(Equipment):
    def add_eq(self, name, quantity):
        super().add_eq(name, eq_type='printer', quantity=quantity)

    def lift_to_warehouse(self, name, quantity):
        super().lift_to_warehouse(name, eq_type = 'printer', quantity=quantity)


class Scaner(Equipment):
    def add_eq(self, name, quantity):
        super().add_eq(name, eq_type='scaner', quantity=quantity)

    def lift_to_warehouse(self, name, quantity):
        super().lift_to_warehouse(name, eq_type = 'scaner', quantity=quantity)


class Xerox(Equipment):
    def add_eq(self, name, quantity):
        super().add_eq(name, eq_type='xerox', quantity=quantity)

    def lift_to_warehouse(self, name, quantity):
        super().lift_to_warehouse(name, eq_type = 'xerox', quantity=quantity)


a = Printer()
x = Xerox()
s = Scaner()
a.add_eq(100, 50)
x.add_eq('Xerox', 100)
s.add_eq('Sony', 150)
a.add_eq('Костян', 500)
a.lift_to_warehouse('Canon', 45)
x.lift_to_warehouse('Xerox', 95)
s.lift_to_warehouse('Sony', 120)
a.lift_to_warehouse('Костян', 450)
w = Warehouse()
w.take_to_subunit('HR Office', 'Canon', 'printer', 40)
w.take_to_subunit('Head Office', 'Xerox', 'xerox', 90)
w.take_to_subunit('Tech Office', 'Sony', 'scaner', 110)
w.take_to_subunit('303 комната', 'Костян', 'printer', 400)
print(f'Структура компании: {structure}')




