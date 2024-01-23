# The get_balance method allows you to retrieve the account balance.

class Balancee:

    def __init__(self, get_balance):
        self.get_balance=get_balance

a=Balancee(1000)
print(f"Account balance: {a.get_balance} AMD")