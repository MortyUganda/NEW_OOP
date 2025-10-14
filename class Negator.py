from functools import singledispatchmethod

class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(data):
        raise TypeError('Аргумент переданного типа не поддерживается')
        
    @neg.register
    @staticmethod
    def _numeric_process(data: int | float):
        return -data
        
    @neg.register
    @staticmethod
    def _str_process(data: bool):
        return not data


