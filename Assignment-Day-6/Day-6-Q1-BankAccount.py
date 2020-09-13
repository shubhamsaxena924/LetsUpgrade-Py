# For this challenge,create a bank account class that has two attributes
#   *ownerName
#   *Balance
# And two methods
#   *deposit
#   *withdraw
# As an added requirement,withdrawals may not exceed the available balance.
# Instantiate your class,make several deposits and withdrawals,and test to make sure the account cant be overdrawn.
class bankAccount():
    def __init__(self, ownerName, Balance):
        self.ownerName = ownerName
        self.Balance = Balance

    def deposit(self, depamt):
        self.Balance = self.Balance + depamt
        print(depamt, 'deposited...')
        return self.Balance

    def withdraw(self, wdamt):
        if wdamt <= self.Balance:
            self.Balance = self.Balance - wdamt
            print(wdamt, 'withdrawn...')
        else:
            print('Your available balance is not enough! ')
        return self.Balance


name = input('Enter Your AccountName: ')
balance = int(input('Enter the balance amount in your account: '))
ownerAccount = bankAccount(name, balance)
dep = int(input('Enter the amount to be deposited: '))
print('Balance = ', ownerAccount.deposit(dep))
wd = int(input('Enter the amount to be withdrawn: '))
print('Balance = ', ownerAccount.withdraw(wd))
print('Thank You! ')
