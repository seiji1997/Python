class Account:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, price):
        self.__balance += price

    def withdraw(self, price):
        if self.__balance < price:
            print("残高が足りません")
        else:
            self.__balance -= price

    def show_balance(self):
        print(f"残高は{self.__balance}円です")


myaccount = Account(10000)
# __balanceは名前修飾(name mangling)されて，_Account__balanceになっている
print(dir(myaccount))
myaccount.deposit(2000)
myaccount.withdraw(5000)
myaccount.withdraw(10000)
# __balanceは_Account__balanceになっているので，「__balanceはない」というエラーになる(balanceも同様)
# print(myaccount.__balance)
# print(myaccount.balance)
# __balanceを更新しようとすると，新たに__balanceが作られる
# __は名前修飾されることを想定しているので，普通は__から始まる変数を更新することはしない
myaccount.__balance = 100000000
print(myaccount.__balance)
print(dir(myaccount))
# __balanceを更新してもself.__balanceは_Account__balanceをさす
myaccount.show_balance()
# 名前修飾はprivate変数として扱うことができるが，更新することは可能
# Pythonではprivate変数を作ることはできない(privateを強制することはしない)
myaccount._Account__balance = 100000000
myaccount.show_balance()