import random 
from datetime import datetime


#Global variable
tax_amount = 0.05
#-------------------

class BankAccount:
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
    
    def check_balances (self):
        return self.balances
    
    
    def print_transactions(self):
        for transaction in self.transaction:
            print(f"\n{transaction['date']}: {transaction['type']} of {transaction['amount']}")

    
    def Print_statement (self):
        print('_________________________________________________________________________')  
        print(f'\nThe account statement for {self.Name}, Account number {self.Account_no}') 
        
        for transactions in self.transaction:
            print(f'\n Time:-{transactions['Date']} ---Type:- {transactions['Type']} ---Amount:- {transactions['amount']}')
    

class SavingAccount(BankAccount):
    pass


class CurrentAccount(BankAccount):
    def deposite(self, amount):
        tax = amount * tax_amount
        return super().deposite(amount - tax_amount)
    
    def withdrawal(self, amount):
        tax = amount * tax_amount
        return super().deposite(amount + tax_amount)

class FixedAccount(BankAccount):
    def __init__(self, Account_no, Name):
        super().__init__(Account_no, Name)
        self.lock = True
        
    def unlock(self):
       self.unlock = True

    def lock(self):
       self.unlock = False

    def withdrawal(self, amount):
        if not self.lock:
            return super().withdrawal(amount)
        
        else:
            print("Withdrawal not allowed: Account is locked.")
    
    
    def print_statement(bank_acc):
        bank_acc.statement()

    def print_balance(bank_acc):
        print(f'{bank_acc.name} balance is {bank_acc.check_balance()}')
        

    
Acc1 = BankAccount ('Harry')
Acc2 = BankAccount('james')
ACC_fixed = FixedAccount('harry')
print(Acc1)
print(Acc2)
#Acc1.deposite(input('\nEnter your amount:'))
#Acc2.deposite(input('\nEnter your amount:'))
Acc1.Print_statement()
Acc2.Print_statement()
print(ACC_fixed)



