import time

start = time.perf_counter()

class Knight:

    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color
    
        self.dct_coordinate = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g':7, 'h':8}
        self.base_x = [el for el in range(8, 0,-1)]
        self.base_y = ['abcdefgh']

        try:
            self.base_position = []
            for y in [1, -1]:
                for x in [2, -2]:
                    self.base_position.append((self.vertical + x, self.dct_coordinate[horizontal] + y))
            for y in [2, -2]:
                for x in [1, -1]:
                    self.base_position.append((self.vertical + x, self.dct_coordinate[horizontal] + y))
        except:
            raise
    
    def get_char(self):
        return 'N'
    
    def can_move(self, can_x, can_y):
        if (self.dct_coordinate[can_x], can_y) in self.base_position:
            return True
        else: return False
    
    def move_to(self, move_x, move_y):
        if (self.dct_coordinate[move_x], move_y) in self.base_position:
            self.horizontal = move_x
            self.vertical = move_y
            try:
                self.base_position = []
                for y in [1, -1]:
                    for x in [2, -2]:
                        self.base_position.append((self.vertical + x, self.dct_coordinate[self.horizontal] + y))
                for y in [2, -2]:
                    for x in [1, -1]:
                        self.base_position.append((self.vertical + x, self.dct_coordinate[self.horizontal] + y))
            except:
                raise
    
    def draw_board(self):
        for y in range(8, 0, -1):
            lst = []
            for x in range(1,9):
                if x == self.dct_coordinate[self.horizontal] and y == self.vertical:
                    lst.append('N')
                elif (y, x) in self.base_position:
                    lst.append('*')
                else:
                    lst.append('.')
            print(*lst, sep='')

knight = Knight('c', 3, 'white')

print(knight.color, knight.get_char())
print(knight.horizontal, knight.vertical)

stop = time.perf_counter()
print(stop - start)