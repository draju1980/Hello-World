# create a bank account class that has two attributes:

# owner
# balance
# and two methods:

# deposit
# withdraw
# As an added requirement, withdrawals may not exceed the available balance.

# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance
  
    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'
  
    def balance(self):
        return self.balance
  
    def deposit(self,deposit):
        self.deposit=deposit
        self.balance=self.balance + self.deposit
        print(f'Deposit Accepted and new balance is {self.balance}')
  
    def withdraw(self,amount):
        self.amount=amount
        if self.balance <= self.amount:
            print(f'{self.owner} insufficient funds in your account')
        else:
            self.balance=self.balance - self.amount
            print(f'Withdrawal Accepted and new balance is {self.balance}')
  