class Numbers: 
    def __init__(self):
        self.lst_even = []
        self.lst_odd = []

    def add_number(self, int_dig):
        if int_dig % 2 == 0:
            self.lst_even.append(int_dig)
        else: self.lst_odd.append(int_dig)

    def get_even(self):
        return [x for x in self.lst_even]
    
    def get_odd(self):
        return [x for x in self.lst_odd]
    

numbers = Numbers()

numbers.add_number(1)
numbers.add_number(2)
numbers.add_number(3)
numbers.add_number(4)

even = numbers.get_even()
odd = numbers.get_odd()
print(numbers.get_even())
print(numbers.get_odd())

even.append(None)
odd.append(None)
print(numbers.get_even())
print(numbers.get_odd())