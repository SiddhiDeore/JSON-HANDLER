from commands import Depositcommand, Withdrawcommand
from account import Account

if __name__=="__main__":

    Account1 = Account(1,1000)
    Account2 = Account(2,1500)

    deposit_money1 = Depositcommand(Account1,2000)
    deposit_money2 = Depositcommand(Account2,400) 

    withdraw1= Withdrawcommand(Account1,500)
    withdraw2 = Withdrawcommand(Account2,1000)

    deposit_money1.execute()
    deposit_money2.execute()
    withdraw1.execute()
    withdraw2.execute()