class Person:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname

    def get_name(self):
        return self._name
    
    def get_surmame(self):
        return self._surname
    
    def set_name(self, name):
        self._name = name
    
    def set_surname(self, surname):
        self._surname = surname

    fullname = property()