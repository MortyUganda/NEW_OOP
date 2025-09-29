class Scales:
    def __init__(self):
        self.x = 0
        self.y = 0

    def add_right(self, b):
        self.x += b

    def add_left(self, a):
        self.y += a

    def get_result(self):
        if self.x == self.y:
            return 'Весы в равновесии'
        elif self.x > self.y:
            return 'Правая чаша тяжелее'
        else:
            return 'Левая чаша тяжелее'
        

scales = Scales()

scales.add_right(1)
scales.add_right(1)
scales.add_left(2)

print(scales.get_result())

