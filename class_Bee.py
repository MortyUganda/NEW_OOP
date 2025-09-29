# Implement the Bee class, which describes a bee that moves on the coordinate plane in four directions: up, down, left, and right. When creating an instance, the class should accept two arguments in the following order:

# x — the bee's coordinate on the x-axis
# x, which defaults to 0
# y — the bee's coordinate on the y-axis
# y, which defaults to 0
# The Bee class instance should have two attributes:

# x is the bee's coordinate on the x-axis
# x
# x
# y is the bee's coordinate on the y-axis
# y
# y
# The Bee class should have four instance methods:

# move_up() is a method that takes an integer n as an argument and increases the bee's coordinate along

# the y—axis by n
# move_down() is a method that takes an integer n as an argument and decreases the bee's coordinate along

# the y—axis by n
# move_right() is a method that takes an integer n as an argument and increasing the bee coordinate on
# the x
# x axis by n
# move_left() is a method that takes an integer n as an argument and reduces the bee coordinate on
# the x
# x axis by n

class Bee:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self, n):
        self.y += n

    def move_down(self, n):
        self.y -= n

    def move_right(self, n):
        self.x += n

    def move_left(self, n):
        self.x -= n


bee = Bee()

bee.move_right(2)
bee.move_right(2)
bee.move_up(3)
bee.move_left(1)
bee.move_down(1)

print(bee.x, bee.y)