# Encapsulation and Private Variables
#  Use underscore _ or double underscore __ to indicate private variables.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500
# print(account.__balance)  # Error: AttributeError
# print(account._BankAccount__balance)  # Error: AttributeError