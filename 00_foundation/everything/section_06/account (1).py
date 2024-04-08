import time


class Account:

    count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.account_number = Account.count
        self.show_balance()
        self.transaction_history = []
        Account.count += 1

    def withdraw(self, price):
        if price <= self.balance:
            self.balance -= price
            self.show_balance()
            self.add_transaction(-price)
        else:
            print(f"残高({self.balance}円)が足りません")

    def deposit(self, price):
        self.balance += price
        self.show_balance()
        self.add_transaction(price)

    def show_balance(self):
        print(f"{self.name}(口座番号:{self.account_number})の残高は{self.balance}円です")

    def add_transaction(self, price):
        transaction = {'withdraw/deposit': price,
                       'new_balance': self.balance,
                       'time': Account.get_time_str()}
        self.transaction_history.append(transaction)

    @staticmethod
    def get_time_str():
        current_time = time.localtime()
        return "{0.tm_year}年{0.tm_mon}月{0.tm_mday}日{0.tm_hour}時{0.tm_min}分".format(current_time)

    def show_transaction_history(self):
        for t in self.transaction_history:
            transaction_str_list = []
            for k, v in t.items():
                transaction_str_list.append(f"{k}: {v}")
            print(", ".join(transaction_str_list))


myaccount = Account(name='my account', balance=0)
myaccount.deposit(10000)
myaccount.withdraw(5000)
myaccount.withdraw(6000)
myaccount.withdraw(3000)
myaccount.deposit(4500)
myaccount.show_transaction_history()





