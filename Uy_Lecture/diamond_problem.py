from abc import ABC, abstractmethod
from random import randint

class Account(ABC):

    @abstractmethod
    def create_account():
        return 0
    @abstractmethod
    def authenticate():
        return 0
    @abstractmethod
    def deposit():
        return 0
    @abstractmethod
    def withdraw():
        return 0
    @abstractmethod
    def display_balance():
        return
    
class SavingsAccount(Account):
    def __init__(self):
        self.savings_accounts = {}
        # key[0] => name   key[1] = Balance
    def create_account(self,name, initial_deposit):
        self.account_number = randint(1000,9999)
        self.savings_accounts[self.account_number] = [name, initial_deposit]
        
    def authenticate(self, name, account_number):
        if account_number in self.savings_accounts.keys():
            if name == self.savings_accounts[account_number][0]:
                print("authentication is Successful...")
                self.account_number = account_number
                return True
            else:
                print("Given name is not Matching")
                return False
        else:
            print("Account Number Does Not exist")
            return False
    def withdraw(self,withdrawal_amount):
        if withdrawal_amount < self.savings_accounts[self.account_number][1]:
            self.savings_accounts[self.account_number][1] -= withdrawal_amount
            print(f"{withdrawal_amount} withdraw successfully..")
        else:
            print("Insufficient Balance")
    def deposit(self,deposit_amount):
        self.savings_accounts[self.account_number][1] += deposit_amount 
        print(f"{deposit_amount} Deposited Successfully")
        
    def display_balance(self):
        print(f"Available Balance: {self.savings_accounts[self.account_number][1]}")
            