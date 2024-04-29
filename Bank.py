import random
from datetime import datetime, date, timedelta

# Global variable for fixed date and tax amount
fixed_date = date(2025, 4, 24)
tax_amount = 0.05

# Base BankAccount class
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
        amount is float
        self.balance += amount
        self.transactions.append({
            'date': datetime.now(),
            'type': 'deposit',
            'amount': amount,
        })
    
    def withdraw(self, amount):
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
            print(f"Date: {transaction['date']} - Type: {transaction['type']} - Amount: {transaction['amount']}")

# CurrentAccount class with additional tax handling
class CurrentAccount(BankAccount):
    def deposit(self, amount):
        tax = amount * tax_amount
        super().deposit(amount - tax)
        self.transactions.append({
            "date": datetime.now(),
            "type": 'tax',
            'amount': tax,
        })
        print(f"{amount - tax} has been deposited successfully")
    
    def withdraw(self, amount):
        tax = amount * tax_amount
        if self.balance >= (amount + tax):
            super().withdraw(amount - tax)
            self.transactions.append({
                "date": datetime.now(),
                "type": 'tax',
                'amount': tax,
            })
            print(f"{amount - tax} has been withdrawn successfully")
        else:
            print("Insufficient balance")

# FixedAccount class with locked withdrawal restrictions
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
            print(f"Date: {transaction['date']} - Type: {transaction['type']} - Amount: {transaction['amount']}")

# Implementation of SavingsPlan class for customizable savings plans
class SavingsPlan:
    def __init__(self, name, target_months, target_amount):
        self.name = name
        self.start_date = datetime.now()
        self.target_months = target_months  # Duration in months
        self.target_amount = target_amount  # Desired savings
        self.current_savings = 0
        self.interest_rate = self.set_interest_rate(target_months, target_amount)
        self.end_date = self.start_date + timedelta(days=30 * target_months)
        self.transactions = []
    
    def set_interest_rate(self, target_months, target_amount):
        if target_months >= 120:
            return 0.12  # 12% interest for 10-year plans
        elif target_months >= 72:
            return 0.10  # 10% interest
        elif target_months >= 36:
            return 0.07  # 7% interest
        elif target_months >= 6:
            if target_amount >= 3000:
                return 0.06  # 6% for savings over 3000
            return 0.05
        elif target_months >= 3:
            if target_amount >= 3000:
                return 0.05
            return 0.04
    
    def deposit(self, amount):
        self.current_savings += amount
        self.transactions.append({
            'date': datetime.now(),
            'type': 'deposit',
            'amount': amount,
        })
    
    def withdraw(self, amount):
        if self.current_savings >= amount:
            self.current_savings -= amount
            self.transactions.append({
                'date': datetime.now(),
                'type': 'withdraw',
                'amount': amount,
            })
        else:
            print("Insufficient funds")
    
    def calculate_interest(self):
        interest = self.current_savings * self.interest_rate
        self.current_savings += interest
        
        self.transactions.append({
            'date': datetime.now(),
                'type': 'interest',
                'amount': interest,
            })
    
    def is_plan_complete(self):
        return datetime.now() >= self.end_date
    
    def plan_summary(self):
        print(f"Savings Plan for: {self.name}")
        print(f"Duration: {self.target_months} months")
        print(f"End Date: {self.end_date}")
        print(f"Interest Rate: {self.interest_rate * 100}%")
        print(f"Current Savings: {self.current_savings}")
        for transaction in self.transactions:
            print(f"Date: {transaction['date']}, Type: {transaction['type']}, Amount: {transaction['amount']}")

# Test section: Create and manage various accounts and savings plans
if __name__ == "__main__":
    # Test BankAccount
    deposit_account = BankAccount("Harry")
    deposit_account.deposit(2000)
    deposit_account.statement()
    deposit_account.withdraw(100)
    deposit_account.statement()  # After withdrawal
    
    # Test CurrentAccount
    current_account = CurrentAccount("James")
    current_account.deposit(300)
    current_account.statement()
    current_account.withdraw(100)
    current_account.statement()  # After withdrawal
    
    # Test FixedAccount
    fixed_account = FixedAccount("Sally")
    fixed_account.statement()
    fixed_account.withdraw(100)  # Should fail due to locked status
    fixed_account.unlock()  # Checking unlock status
    
    # Test SavingsPlan with user inputs
    def create_savings_plan():
        name = input("Enter your name: ")
        target_months = int(input("Enter the number of months you want to save: "))
        target_amount = float(input("Enter the target amount you want to save: "))
        
        plan = SavingsPlan(name, target_months, target_amount)
        initial_deposit = float(input("Enter the amount you want to deposit: "))
        plan.deposit(initial_deposit)
        
        # Apply interest and print summary
        plan.calculate_interest()
        plan.plan_summary()
        
        return plan
    
    # Create a new savings plan
    new_plan = create_savings_plan()  # User input required

    # Simulate additional deposits and calculate interest
    new_plan.deposit(1000)  # Additional deposit
    new_plan.calculate_interest()  # Reapply interest
    new_plan.plan_summary()  # Summary with new deposit
