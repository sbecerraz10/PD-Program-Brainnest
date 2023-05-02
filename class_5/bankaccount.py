class BankAccount:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number
    
    def deposit(self, amount):
        self.balance += amount
        return amount, self.balance
    
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("The process couldn't be completed")
        return amount, self.balance
    
    def info(self):
        return f"Your account {self.account_number} has {self.balance} dollars"
    
myAccount = BankAccount(balance=23000, account_number="389290345")
print(myAccount.info())
amount, balance = myAccount.deposit(2000)
print(f"You deposited {amount} dollars, your new balance is {balance}")
amount, balance = myAccount.withdraw(300)
print(f"You withdrew {amount} dollars, your new balance is {balance}")
print(myAccount.info())
    