# Implement the Vector class, which describes a vector on a plane. When creating an instance, the class 
# should accept two arguments in the following order:
# An instance of the Vector class should have the following formal string representation:

# Vector(<x coordinate>, <y coordinate>)

# Additionally, instances of the Vector class should support comparison operations using the == and!= operators. 
# Two vectors are considered equal if their coordinates on both axes are the same. 
# Methods that implement comparison operations must be able to compare both two vectors with each other and a vector 
# with a tuple of two numbers representing the coordinates

class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Vector({self.x}, {self.y})'
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Vector):
            return self.x == value.x and self.y == value.y
        if isinstance(value, tuple) and len(value) == 2:
            return self.x == value[0] and self.y == value[1]
        return NotImplemented


# Sample Input 1:

a = Vector(1, 2)
b = Vector(1, 2)

print(a == b)
print(a != b)
# Sample Output 1:

# True
# False