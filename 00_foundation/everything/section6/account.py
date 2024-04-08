class Account:

    count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.account_number = Account.count
        self.show_balance()
        Account.count += 1

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.show_balance()
        else:
            print(f"残高({self.balance}円)が足りません")

    def deposit(self, amount):
        self.balance += amount
        self.show_balance()

    def show_balance(self):
        print(f"{self.name}(口座番号:{self.account_number})の残高は{self.balance}円です")


myaccount = Account(name='my account', balance=0)
myaccount.deposit(10000)
myaccount.withdraw(5000)
