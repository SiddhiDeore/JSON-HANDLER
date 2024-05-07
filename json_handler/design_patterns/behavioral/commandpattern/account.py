
class Account:
    def __init__(self,account_id,balance) -> None:
        self.account_id = account_id
        self.balance =balance
    
    def deposit(self,amount):
        self.balance +=amount
        print(f"Depoaited Rs.{amount} to bank account {self.account_id}.New balance is {self.balance}")

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"Withrawed Rs.{amount} to bank account {self.account_id}.New balance is {self.balance}")
        else:
            print(f"Not enough balance!")