class ACCOUNT:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self, amount):
        self.balance+=amount
        print(f"Deposited {amount},Balance: {self.balance}")
    def withdrawl(self, amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"withdrawlamount {amount},Balance: {self.balance}")
        else:
            print("Insufficient balance")
class savings_account(ACCOUNT):
    def __init__(self, name,balance,intrest_rate):
        super().__init__(name,balance)
        self.intrest_rate=intrest_rate
    def add_intrest(self):
        intrest=self.balance*self.intrest_rate
        self.balance+=intrest
        print(f"TOTALINTEREST {intrest},Balance: {self.balance}")
class current_account(ACCOUNT):
    def __init__(self,name,balance,negative_amount_allowance):
        super().__init__(name,balance)
        self.negative_amount_allowance=negative_amount_allowance
        def withdrawl(self,amount):
            if amount<=self.balance + self.negative_amount_allowance:
                self.balance-=amount
                print(f"withdrawl amount{amount},Balance: {self.balance}")
            else:
                print("limit exceed")
s=savings_account("sairam",9000,0.10)
s.deposit(3000)
s.withdrawl(7000)
s.add_intrest()
print()
c=current_account("sai",4000,2000)
c.deposit(200)
c.withdrawl(500)