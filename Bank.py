import random
from datetime import datetime, date

# Global variable for fixed date and tax amount
fixed_date = date(2025, 4, 24)
tax_amount = 0.05

class BankAccount:
    def __init__(self, name):
        self.account_number = self.generate_acct()
        self.name = name
        self.transactions = []
        self.balance = 0
  
    def generate_acct(self):
        digit = [str(random.randint(0, 9)) for _ in range(10)]
        acct = ''.join(digit)
        return acct
  
    def deposit(self, amount):
        amount = float(amount)
        self.balance += amount
        self.transactions.append({
            'date': datetime.now(),
            'type': 'deposit',
            'amount': amount,
        })
    
    def withdraw(self, amount):
        amount = float(amount)
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append({
                'date': datetime.now(),
                'type': 'withdraw',
                'amount': amount,
            })
        else:
            print("Insufficient balance")
    
    def check_balance(self):
        return self.balance  
    
    def statement(self):
        print(f'Account No: {self.account_number} --- Name: {self.name}')
        for transaction in self.transactions:
            print(f"Date: {transaction['date']} - Type: {transaction['type']} - Amount: {transaction['amount']}\n")

class CurrentAccount(BankAccount):
    def deposit(self, amount):
        tax = amount * tax_amount
        super().deposit(amount - tax)
        self.transactions.append({
            "date": datetime.now(),
            "type": 'tax',
            'amount': tax,
        })
    
    def withdraw(self, amount):
        tax = amount * tax_amount
        if self.balance >= (amount + tax):
            super().withdraw(amount - tax)
            self.transactions.append({
                "date": datetime.now(),
                "type": 'tax',
                'amount': tax,
            })
        else:
            print("Insufficient balance")

class FixedAccount(BankAccount):
    def __init__(self, name):
        super().__init__(name)
        self.locked_until = fixed_date

    def withdraw(self, amount):
        if datetime.now().date() < self.locked_until:
            print(f"Account is locked until {self.locked_until}. Withdrawal not allowed.")
        else:
            super().withdraw(amount)

    def unlock(self):
        if datetime.now().date() >= self.locked_until:
            return True
        return False
  
    def statement(self):
        print(f'Account No: {self.account_number} --- Name: {self.name}')
        for transaction in self.transactions:
            print(f"Date: {transaction['date']} - Type: {transaction['type']} - Amount: {transaction['amount']}\n")

# Test statements for Current and Fixed accounts
current_account = CurrentAccount("Alice")
current_account.deposit(200)
current_account.withdraw(50)
print("Current Account Statement:")
current_account.statement()

fixed_account = FixedAccount("Bob")
fixed_account.deposit(500)
fixed_account.withdraw(100)  # Should print that withdrawal is not allowed
print("Fixed Account Statement:")
fixed_account.statement()
import random
from datetime import datetime, date

# Global variable for fixed date and tax amount
fixed_date = date(2025, 4, 24)
tax_amount = 0.05

class BankAccount:
    def __init__(self, name):
        self.account_number = self.generate_acct()
        self.name = name
        self.transactions = []
        self.balance = 0
  
    def generate_acct(self):
        digit = [str(random.randint(0, 9)) for _ in range(10)]
        acct = ''.join(digit)
        return acct
  
    def deposit(self, amount):
        amount = float(amount)
        self.balance += amount
        self.transactions.append({
            'date': datetime.now(),
            'type': 'deposit',
            'amount': amount,
        })
    
    def withdraw(self, amount):
        amount = float(amount)
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append({
                'date': datetime.now(),
                'type': 'withdraw',
                'amount': amount,
            })
        else:
            print("Insufficient balance")
    
    def check_balance(self):
        return self.balance  
    
    def statement(self):
        print(f'Account No: {self.account_number} --- Name: {self.name}')
        for transaction in self.transactions:
            print(f"Date: {transaction['date']} - Type: {transaction['type']} - Amount: {transaction['amount']}\n")

class CurrentAccount(BankAccount):
    def deposit(self, amount):
        tax = amount * tax_amount
        super().deposit(amount - tax)
        self.transactions.append({
            "date": datetime.now(),
            "type": 'tax',
            'amount': tax,
        })
    
    def withdraw(self, amount):
        tax = amount * tax_amount
        if self.balance >= (amount + tax):
            super().withdraw(amount - tax)
            self.transactions.append({
                "date": datetime.now(),
                "type": 'tax',
                'amount': tax,
            })
        else:
            print("Insufficient balance")

class FixedAccount(BankAccount):
    def __init__(self, name):
        super().__init__(name)
        self.locked_until = fixed_date

    def withdraw(self, amount):
        if datetime.now().date() < self.locked_until:
            print(f"Account is locked until {self.locked_until}. Withdrawal not allowed.")
        else:
            super().withdraw(amount)

    def unlock(self):
        if datetime.now().date() >= self.locked_until:
            return True
        return False
  
    def statement(self):
        print(f'Account No: {self.account_number} --- Name: {self.name}')
        for transaction in self.transactions:
            print(f"Date: {transaction['date']} - Type: {transaction['type']} - Amount: {transaction['amount']}\n")

# Test statements for Current and Fixed accounts
current_account = CurrentAccount("Alice")
current_account.deposit(200)
current_account.withdraw(50)
print("Current Account Statement:")
current_account.statement()

fixed_account = FixedAccount("Bob")
fixed_account.deposit(500)
fixed_account.withdraw(100)  # Should print that withdrawal is not allowed
print("Fixed Account Statement:")
fixed_account.statement()
