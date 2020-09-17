import sys

class BankAccount:
    minimum_balance = 1000

    def __init__(self, account_name, account_number, bvn, balance):
        self.account_name = account_name
        self.account_number = BankAccount.validate_account_number(account_number)
        self.bvn = bvn
        self.balance = balance

    def get_account_name(self):
        return self.account_name

    def get_account_number(self):
        return self.account_number

    def get_bvn(self):
        return self.bvn
   
    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount >= self.balance:
            print('Insufficient funds')
        elif (self.balance - amount) < BankAccount.minimum_balance:
            print('Balance must not be less than 1000')
        else:
            self.balance -= amount

    @staticmethod
    def validate_account_number(account_number):
        size = len(account_number)
        if size < 10 or size > 10:
            print('Account number must be 10 characters')
            sys.exit()
        elif type(int(account_number)) != int:
            print('Account number must be a number')
            sys.exit()
        else:
            return account_number 