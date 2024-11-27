class Account:
    def __init__(self , number:int, holder: str, balance: float):
        self.number= number
        self.holder=holder
        self.balance=balance
    def withdraw(self , amont:float):
        if self.balance> amont:
            saldo= amont>0 and self.balance-amont
            print("seu saldo é de " , saldo)
        
        elif - amont:
            print ('saldo insuficiente')





        
    def deposit (self, amount: float):
        if amount >0:
            self.balance+=amount

        else :
            print ("valor invalido")

class BussineAccout(Account):
    def __init__(self, number: int, holder: str, balance: float, loanLimit:int):
        super().__init__(number, holder, balance)
        self.loanLimit= loanLimit
    def loan(self , amont: float):
        if amont> a and amont<=  self.loanLimit:
            self.balance+= amont
        else:
            print("valor invalido")
         


# ale = Account( 45,"sdfsf",13)
# ale.withdraw(12)