# CHALLENGE PROBLEM:

# For this challenge, create a bank account class that has two attributes:
# • Owner
# • Balance
# and two methods:
# • Deposit
# • Withdraw
# As an added requirement, withdrawals may not exceed the available balance. Instantiate your class,
# make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class bankAccount():
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amountToDeposit):
        if amountToDeposit > 0:
            self.balance += amountToDeposit
            return "Successfully deposited: " + str(amountToDeposit) + " $"
        else:
            return "Invalid deposit amount "

    def withdraw(self, amountToWithdraw):
        if amountToWithdraw > 0:
            if amountToWithdraw <= self.balance:
                self.balance -= amountToWithdraw
                return "Successfully withdrew: " + str(amountToWithdraw) + " $"
            else:
                return "Insufficient funds, try again "
        else:
            return "Invalid withdrawal amount"

    def __str__(self):
        return "Owner name: " + self.owner + " |-|-|-|-|-| Available balance in $: " + str(self.balance)

######## Testing the bankAccount class
myAccount = bankAccount("Victor", 95)
print(myAccount)
print(myAccount.owner)
print(myAccount.balance)

print(myAccount.deposit(100))
print(myAccount)
print(myAccount.withdraw(195))

### Trying to overdraw
print(myAccount.withdraw(300))
print(myAccount)