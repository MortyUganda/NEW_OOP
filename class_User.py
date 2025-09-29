# You have access to the House class, which describes a house. When creating an instance, the class takes two arguments in the following order:

# color — the color of the house
# rooms — the number of rooms in the house
# An instance of this class has two attributes:

# color — the color of the house
# rooms — the number of rooms in the house
# Implement two instance methods for the House class:

# paint() is a method that takes a new_color argument and changes the current color of the house to new_color
# add_rooms() is a method that takes an integer n argument and increases the number of rooms in the house by n

class House:
    def __init__(self, color, rooms):
        self.color = color
        self.rooms = rooms
    def paint(self, new_color):
        self.color = self.new_color

    def add_rooms(self, n):
        self.rooms += n

house = House('white', 4)

print(house.color)
print(house.rooms)