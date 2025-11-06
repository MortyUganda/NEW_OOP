# Implement the Money class, which describes the amount of money in rubles. When creating an instance, the class must take one argument.:

# amount — the amount of money
# An instance of the Money class must have the following informal string representation:

# <amount of money> rub.

                  
# Also, an instance of the Money class must support the unary operators + and -:

# the result of the unary + should be a new instance of the Money class with a non-negative amount of money
# the result of the unary - should be a new instance of the Money class with a negative amount of money

class Money:
    def __init__(self, amount) -> None:
        self.amount = amount
    def __neg__(self):
        return __class__(-self.amount)
    def __pos__(self):
        return __class__(self.amount)
    
    def __str__(self) -> str:
        return f'{self.amount} руб.'
    

# Sample Input 1:

money = Money(100)

print(money)
print(+money)
print(-money)

# Sample Output 1:

# 100 руб.
# 100 руб.
# -100 руб.