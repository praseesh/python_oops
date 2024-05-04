from abc import ABC, abstractmethod

# Abstract class
class Account(ABC):
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.balance

# Concrete classes
class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

class CurrentAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=1000):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

# Usage
savings_acc = SavingsAccount("SAV-123")
savings_acc.deposit(1000)
savings_acc.add_interest()
print("Savings Account Balance:", savings_acc.get_balance())

current_acc = CurrentAccount("CUR-456")
current_acc.deposit(500)
current_acc.withdraw(700)
print("Current Account Balance:", current_acc.get_balance())
