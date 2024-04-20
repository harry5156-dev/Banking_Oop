import random 
from datetime import datetime

class AccountInfo:
    def __init__(self, Name):
        self.Account_no = self.generate_account() 
        self.Name = Name 
        self.transaction = []
        self.balances = 0
        
        
    def generate_account(self):
        digit = []
        for _ in range (10):
            rand_num = random.randint(0, 9)
            digit.append(str(rand_num))
        
        New_account_no = "".join(digit)
        return New_account_no
    
    
    def deposite (self, amount):
        amount = float(amount)
        self.balances = self.balances + amount
        self.transaction.append({
            'Date': datetime.now(),
            'Type': 'Deposit',
            'amount':amount,
            }
        )
        
    def withdrawal (self, amount):
        amount = float(amount)
        self.balances = self.balances - amount
        self.transaction.append({
            'Date': datetime.now(),
            'Type': 'Withdrawal',
            'amount': amount
        })  
        
    
        
        
        
        
    
    def __str__(self) -> str:
        return f"the name is {self.Name} and the account number is {self.Account_no}"
    
    
    


Acc1 = AccountInfo ('Harry')
Acc1.deposite(input('Enter your account info:'))
print(Acc1)

