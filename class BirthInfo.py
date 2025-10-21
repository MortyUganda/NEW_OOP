from functools import singledispatchmethod
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta


class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date) -> None:
        raise TypeError('Аргумент переданного типа не поддерживается')

#экземпляр класса date
    @__init__.register(date)
    def _(self, birth_date):
        self.birth_date = birth_date

#строка с датой в ISO формате
    @__init__.register(str)
    def _(self, birth_date):
        try:
            self.birth_date = date.fromisoformat(birth_date)
        except:
            raise TypeError('Аргумент переданного типа не поддерживается')

#список или кортеж из трех целых чисел: года, месяца и дня
    @__init__.register(list | tuple)
    def _(self, birth_date):
        try:
            year, month, day = birth_date
            if all(map(lambda x: type(x) == int, birth_date)):
                self.birth_date = date.fromisoformat('-'.join([str(el).zfill(2) for el in birth_date]))
            else: raise TypeError('Аргумент переданного типа не поддерживается')
        except:
            raise TypeError('Аргумент переданного типа не поддерживается')
        

    @property
    def age(self):
        return relativedelta(date.today(), self.birth_date).years


birth_dates = [
    [2020],
    (2020,),
    [2020, 1],
    [2020, 1, '1'],
    (2020, 1),
    (2020, 1, '1'),
    [2020, 1, 1, 1],
    (2020, 1, 1, 1),
    [2020, '1', '1'],
    [2020, '1', 1],
]

for birth_date in birth_dates:
    try:
        birthinfo = BirthInfo(birth_date)
    except TypeError as e:
        print(e)
