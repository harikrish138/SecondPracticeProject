class Bank:
    def __init__(self,name,balance):
        self._name=name
        self._balance=balance
        print('Name : ',name,'\nBalance : ',balance)

class BankName(Bank):
    def deposite(self,balance):
        self._balance += balance
        print('Account balance : ',self._balance)
    def withdraw(self,amount):
        self._balance -= amount
        print('Total available balance : ',self._balance)
    def CheckBalance(self):
        print('Account holder name : ',self._name)
        print('Total available balance : ',self._balance)

# obj1 = Bank('Ravi',10000)
obj= BankName('Ravi',12000)
obj.withdraw(5000)
obj.deposite(15000)
obj.CheckBalance()