class Person:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname

    def get_name(self):
        return self.name + ' ' + self.surname
    
    def set_name(self, info):
        self.name, self.surname = info.split()

    fullname = property(get_name, set_name)
