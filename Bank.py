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
    
    def transfer(self, bank_account):
        pass

    
    def print_transactions(self):
        for transaction in self.transaction:
            print(f"\n{transaction['date']}: {transaction['type']} of {transaction['amount']}")

    
    def check_balances (self):
        return self.balances
    
    
    def Print_statement (self):
        print('_________________________________________________________________________')  
        print(f'\nThe account statement for {self.Name}, Account number {self.Account_no}') 
        print('_________________________________________________________________________')  
        for transactions in self.transaction:
            print(f'\n{transactions['Date']} --- {transactions['Type']} --- {transactions['amount']}')
    

    


Acc1 = AccountInfo ('Harry')
Acc2 = AccountInfo('james')
print(Acc1)  
print(Acc2)
Acc1.deposite(input('\nEnter your amount:'))
Acc2.deposite(input('\nEnter your amount:'))
Acc1.Print_statement()
Acc2.Print_statement()


