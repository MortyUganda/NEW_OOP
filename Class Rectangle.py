class Rectangle:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
    
    def get_periment(self):
        return self.length * 2 + self.width
    
    def get_area(self):
        return self.length * self.width
    
    perimetr = property(get_periment)
    area = property(get_area)