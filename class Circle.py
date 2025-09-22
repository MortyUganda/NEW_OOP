# Implement the Circle class, which describes a circle. When creating an instance, the class should accept one argument:

# radius — the radius of the circle
# An instance of the Circle class should have three attributes:

# _radius — the radius of the circle
# _diameter — the diameter of the circle
# _area — the area of the circle
# The Circle class should have three instance methods:

# get_radius() — a method that returns the radius of the circle
# get_diameter() — a method that returns the diameter of the circle
# get_area() — a method that returns the area of the circle

from math import pi

class Circle:
    def __init__(self, radius):
        self._radius = radius 
        self._diameter = radius * 2
        self._area = pi * radius**2
    def get_radius(self):
        return self._radius
    def get_diameter(self):
        return self._diameter
    def get_area(self):
        return self._area
    
circle = Circle(5)

print(circle.get_radius())
print(circle.get_diameter())
print(round(circle.get_area()))