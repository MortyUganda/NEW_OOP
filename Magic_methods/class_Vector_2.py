# Implement the Vector class, which describes a vector on a plane. When creating an instance, the class must accept two arguments in the following order:

# the x — coordinate of the vector on the x axis x
# the y — coordinate of the vector on the y axis y
# An instance of the Vector class must have the following formal string representation:

# Vector(<x coordinate>, <y coordinate>)
        
# And the following informal string representation:

# (<x-axis vector coordinate>, <y-axis vector coordinate>)
              
# Also, an instance of the Vector class must support the unary operators + and -:

# the result of the unary + should be a new instance of the Vector class with the original coordinates
# the result of the unary - should be a new instance of the Vector class with coordinates taken with the opposite sign
# Finally, when passing an instance of the Vector class to the abs() function, its module must be returned.

class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'
    
    def __repr__(self) -> str:
        return f'Vector({self.x}, {self.y})'
    
    def __neg__(self):
        return Vector(-self.x, -self.y)
    
    def __pos__(self):
        return Vector(self.x, self.y)
    
    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5
    
# Sample Input:

vector = Vector(3, -4)

print(+vector)
print(-vector)
print(abs(vector))

# Sample Output:

# (3, -4)
# (-3, 4)
# 5.0