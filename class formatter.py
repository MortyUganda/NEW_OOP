from functools import singledispatchmethod

class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError('Аргумент переданного типа не поддерживается')
    
    @format.register
    @staticmethod
    def int_process(data: int):
        print(f'Целое число: {data}')
        
    @format.register
    @staticmethod
    def _float_process(data: float):
        print(f'Вещественное число: {data}')
    @format.register
    @staticmethod
    def tuple_process(data: tuple):
        print(f'Элементы кортежа: {', '.join([str(i) for i in data])}')

    @format.register
    @staticmethod
    def list_process(data: list):
        print(f'Элементы списка: {', '.join([str(i) for i in data])}')

    @format.register(dict)
    @staticmethod
    def _(data):
        print(f'Пары словаря: {", ".join(str(i) for i in data.items())}')


Formatter.format(1337)
Formatter.format(20.77)

Formatter.format([10, 20, 30, 40, 50])
Formatter.format(([1, 3], [2, 4, 6]))

Formatter.format({'Cuphead': 1, 'Mugman': 3})
Formatter.format({1: 'one', 2: 'two'})
Formatter.format({1: True, 0: False})