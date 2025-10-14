class CaseHelper :

    @staticmethod
    def is_snake(stroka: str):
        if '_' in stroka or stroka.islower():
            return True
        else: 
            return False

    @staticmethod
    def is_upper_camel(stroka: str):
        if stroka[0].isupper():
            return True
        else: 
            return False

    @staticmethod
    def to_snake(stroka: str):
        temp = [el for el in stroka if el.isupper()]
        if len(temp) == 1:
            return stroka.title().lower()
        else:
            pass
    @staticmethod
    def to_upper_camel(stroka: str):
        pass

print(CaseHelper.is_snake('beegeek'))
print(CaseHelper.is_snake('bee_geek'))
print(CaseHelper.is_snake('Beegeek'))
print(CaseHelper.is_snake('BeeGeek'))
print()
print(CaseHelper.is_upper_camel('beegeek'))
print(CaseHelper.is_upper_camel('bee_geek'))
print(CaseHelper.is_upper_camel('Beegeek'))
print(CaseHelper.is_upper_camel('BeeGeek'))

print(CaseHelper.to_snake('Beegeek'))
print(CaseHelper.to_snake('BeeGeek'))