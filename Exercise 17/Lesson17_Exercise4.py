# We create an Object of the BankAccount class called account1 with an initial balance of $1000.

class BankAccount:

    def __init__(self, account1=1000):
        self.account1=account1

a=BankAccount()
print(f"initial balance: {a.account1} USD")