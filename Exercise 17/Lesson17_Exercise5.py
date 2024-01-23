# # We deposit $500 and withdraw $200 from the account and print the account information.

class AccountInformation:
    
    def depp(self,deposit=500,withdraw=200):
        self.deposit=deposit
        self.withdraw=withdraw
        return self.deposit-self.withdraw
    
userinfo=AccountInformation()
print(userinfo.depp())


# class AccountInformation:

#     def __init__(self,deposit=500, withdraw=200):
#             self.deposit=deposit
#             self.withdraw=withdraw

#     def infoo(self):
#         return f"AccountInformation: {self.deposit-self.withdraw} USD"

# userinfo=AccountInformation()
# print(userinfo.infoo())

# ############# կամ 

# class AccountInformation:

#     def __init__(self,deposit):
#             self.deposit=deposit

#     def withh(self,withdraw):
#          self.withdraw=withdraw

#     def infoo(self):
#         return f"AccountInformation: {self.deposit-self.withdraw} USD"

# userinfo=AccountInformation(500)
# userinfo.withh(200)
# print(userinfo.infoo())