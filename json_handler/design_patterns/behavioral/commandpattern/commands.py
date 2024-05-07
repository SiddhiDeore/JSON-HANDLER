from abc import ABC,abstractclassmethod

class Command(ABC):
    def execute(self):
        pass

class Depositcommand(Command):
    def __init__(self,account,amount) -> None:
        self.account = account
        self.amount = amount
    
    def execute(self):
        self.account.deposit(self.amount)

class Withdrawcommand(Command):
    def __init__(self,account,amount) -> None:
        self.account=account
        self.amount = amount

    def execute(self):
        self.account.withdraw(self.amount)



