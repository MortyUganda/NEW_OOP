# Implement the Circle class, which describes a circle. When creating an instance, the class should accept one argument:

# radius — the radius of the circle
# An instance of the Circle class should have three attributes:

# radius — the radius of the circle
# diameter — the diameter of the circle
# area — the area of the circle

from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius * 2
        self.area = pi * radius**2

circle = Circle(5)

print(circle.radius)
print(circle.diameter)
print(circle.area)