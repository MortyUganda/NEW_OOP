# Implement the ReversibleString class that describes the string. When creating an instance, the class must take one argument.:

# string — the value of the string
# An instance of the ReversibleString class must have the following informal string representation:

# <string value>

                  
# Also, an instance of the ReversibleString class must support the unary operator -, which should result in a new 
# instance of the ReversibleString class with the string value in reverse order.


class ReversibleString:
    def __init__(self, string) -> None:
        self.string = string
        
    def __str__(self) -> str:
        return str(self.string)
    
    def __neg__(self):
        return ReversibleString(self.string[::-1])


# Sample Input:

string = ReversibleString('python')

print(string)
print(-string)

# Sample Output:

# python
# nohtyp

