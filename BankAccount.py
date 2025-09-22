# Implement the BankAccount class, which describes a bank account. When creating an instance, the class should accept one argument:

# balance — the account balance, which defaults to 0
# The BankAccount class instance should have one attribute:
# _balance — the account balance

# The BankAccount class should have four instance methods:
# get_balance() — a method that returns the current account balance
# deposit() — a method that takes an amount argument and increases the account balance by amount
# withdraw() is a method that takes the amount number as an argument and reduces the account balance by amount.
# If the amount exceeds the amount of funds in the account balance, a ValueError exception should be raised with the message:
# There are insufficient funds in the account

 
# transfer() is a method that takes as arguments the bank account account and the amount number. 
# The method should decrease the current account balance by amount and increase the account balance by amount. 
# If the amount exceeds the amount of funds in the balance, then

class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else: 
            raise ValueError('На счете недостаточно средств')

    def transfer(self, account, amount):
        if amount <= self._balance:
            self.withdraw(amount)
            account.deposit(amount)
        else: 
            raise ValueError('На счете недостаточно средств') 


account1 = BankAccount(balance=100)
account2 = BankAccount()
account1.transfer(account2, 100)
print(account1.get_balance())
print(account2.get_balance())