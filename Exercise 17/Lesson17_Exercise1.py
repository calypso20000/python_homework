# Define a class named BankAccount with an __init__ method that initializes two instance variables: account_holder and balance.

class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder=account_holder
        self.balance=balance

a=BankAccount(account_holder="CALYPSO AFRIKYAN", balance="1.000.000 AMD")
print(f"Բանկի օգտատեր։ {a.account_holder}, \nՀաշվի մնացորդ։ {a.balance}")