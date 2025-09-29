# Implement a Person class that describes a person. When creating an instance, the class should accept two arguments in the following order:

# name — the person's name
# surname — the person's last name
# An instance of the Person class should have two attributes:

# name — the person's name
# surname — the person's last name
# The Person class should have one property:

# fullname — a read-write property that returns the person's full name as a string: 
# <name> <last name>

class Person:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname

    def get_name(self):
        return self.name + ' ' + self.surname
    
    def set_name(self, info):
        self.name, self.surname = info.split()

    fullname = property(get_name, set_name)

person = Person('Меган', 'Фокс')

print(person.name)
print(person.surname)
print(person.fullname)

# Меган
# Фокс
# Меган Фокс